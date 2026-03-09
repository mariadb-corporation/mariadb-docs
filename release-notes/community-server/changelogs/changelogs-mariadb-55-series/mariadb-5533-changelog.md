# MariaDB 5.5.33 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.33) |[Release Notes](../../old-releases/5.5/5.5.33.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 17 Sep 2013

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.33.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3896.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3896.1.1)\
  Mon 2013-09-16 21:21:15 +0200
  * specify deb conflicts correctly
* [Revision #3896](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3896)\
  Fri 2013-09-13 23:42:29 +0200
  * fix BUILD/compile-solaris-amd64 to produce working binaries
* [Revision #3895](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3895)\
  Fri 2013-09-13 23:42:00 +0200
  * [MDEV-5012](https://jira.mariadb.org/browse/MDEV-5012) Server crashes in Item\_ref::real\_item on EXPLAIN with select subqueries or views, constant table, derived\_merge+derived\_with\_keys
* [Revision #3894](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3894) \[merge]\
  Fri 2013-09-13 14:47:40 +0400
  * Null-merge from 5.3.
  * [Revision #2502.567.136](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.136)\
    Fri 2013-09-13 14:43:10 +0400
    * [MDEV-4724](https://jira.mariadb.org/browse/MDEV-4724) Some temporal functions do not preserve microseconds
* [Revision #3893](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3893) \[merge]\
  Fri 2013-09-13 13:19:29 +0300
  * merge 5.3->5.5
  * [Revision #2502.567.135](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.135)\
    Thu 2013-09-12 17:05:29 +0300
    * [MDEV-5005](https://jira.mariadb.org/browse/MDEV-5005): Subquery in Procedure somehow affecting temporary table
* [Revision #3892](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3892) \[merge]\
  Fri 2013-09-13 12:06:17 +0400
  * Merge from 5.3.
  * [Revision #2502.579.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.579.1)\
    Thu 2013-09-12 21:31:14 +0400
    * [MDEV-4724](https://jira.mariadb.org/browse/MDEV-4724) Some temporal functions do not preserve microseconds
* [Revision #3891](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3891) \[merge]\
  Thu 2013-09-12 13:54:46 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.567.134](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.134)\
    Thu 2013-09-12 13:53:13 +0400
    * [MDEV-5011](https://jira.mariadb.org/browse/MDEV-5011): ERROR Plugin 'MEMORY' has ref\_count=1 after shutdown for SJM queries - Provide a special execution path for cleanup of degenerate non-merged semi-join children of degenerate selects.
* [Revision #3890](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3890)\
  Thu 2013-09-12 10:10:09 +0200
  * tokudb buildbot fixes
* [Revision #3889](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3889)\
  Wed 2013-09-11 15:35:49 +0200
  * support ./mtr suite.test,com,bi,na,tions syntax
* [Revision #3888](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3888) \[merge]\
  Tue 2013-09-10 23:02:25 +0200
  * merge with 5.5-tokudb tree (TokuDB 7.0.4). In particular:
    * add TokuDB, together with the ft-index library
    * cmake support, auto-detecting whether tokudb can be built
    * fix packaging - tokudb-engine.rpm, deb
    * remove PBXT
    * add jemalloc
    * the server is built with jemalloc by default even if TokuDB is not built
    * documentation files in RPM are installed in the correct location
    * support for optional deb packages (tokudb has specific build requirements)
    * move plugins from mariadb-server deb to appropriate debs (server/test/libmariadbclient)
    * correct mariadb-test.deb to be not architecture-independent
    * fix out-of-tree builds to never modify in-tree files
    * new handler::prepare\_index\_scan() method
* [Revision #3887](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3887)\
  Tue 2013-09-10 11:04:14 +0200
  * fix insert.test in `--ps-protocol`.
* [Revision #3886](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3886) \[merge]\
  Tue 2013-09-10 10:08:11 +0400
  * Merge from 5.3
  * [Revision #2502.567.133](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.133)\
    Mon 2013-09-09 15:32:25 +0400
    * [MDEV-4863](https://jira.mariadb.org/browse/MDEV-4863) COALESCE(time\_or\_datetime) returns wrong results in numeric context
* [Revision #3885](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3885)\
  Mon 2013-09-09 19:31:29 +0200
  * [MDEV-4941](https://jira.mariadb.org/browse/MDEV-4941) make: AIX fails with 'Identifier not allowed in cast'; syntax error in include/my\_global.h
* [Revision #3884](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3884)\
  Mon 2013-09-09 16:56:35 +0500
  * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Audit-plugin. Server-related part of the task. file\_logger became the service. Data like query\_id now are sent to the audit plugin. Fix for [MDEV-4770](https://jira.mariadb.org/browse/MDEV-4770) ported from 10.0. Fix added for the read\_maria\_plugin\_info(). Log rotation can be disabled with 'set rotations=0'.
* [Revision #3883](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3883)\
  Sun 2013-09-08 11:36:34 +0200
  * fix for xtradb to compile on windows
* [Revision #3882](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3882)\
  Sat 2013-09-07 22:36:34 +0200
  * fix xtradb to compile in both debug and optimized builds
* [Revision #3881](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3881) \[merge]\
  Sat 2013-09-07 13:49:15 +0200
  * Percona-Server-5.5.33-rel31.1.tar.gz
  * [Revision #0.12.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.64)\
    Sat 2013-09-07 09:47:42 +0200
    * Percona-Server-5.5.33-rel31.1.tar.gz
* [Revision #3880](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3880) \[merge]\
  Fri 2013-09-06 22:31:30 +0200
  * mysql-5.5.33 merge
  * [Revision #3077.188.78](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.78)\
    Mon 2013-07-15 13:41:27 +0200
    * Removed random passwords feature for Bugfix#17160741 (not applicable for 5.5.X)
  * [Revision #3077.188.77](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.77)\
    Wed 2013-07-10 19:14:41 +0200
    * Updated spec file for Bug#17080138
  * [Revision #3077.188.76](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.76)\
    Tue 2013-07-09 20:35:26 +0200
    * Removed directory /usr/share/mysql/solaris/postinstall-solaris to resolve build error
  * [Revision #3077.188.75](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.75)\
    Fri 2013-07-05 14:30:15 +0530
    * Bug#17033706 SINCE 5.5.32 & 5.6.12, INNODB CANT START WITH OWN MULTI-FILE TABLESPACE
  * [Revision #3077.188.74](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.74)\
    Thu 2013-07-04 16:59:09 +0530
    * Bug #16567381 DATETIME FIELD COMPARISONS DO NOT WORK PROPERLY WITH UTF8\_UNICODE\_CI COLLATION Problem Description: When comparing datetime values with strings, the utf8\_unicode\_ci collation prevents correct comparisons. Consider the below set of queries, it is not showing any results on a table which has tuples that satisfies the query. But for collation utf8\_general\_ci it shows one tuple. `set names utf8 collate utf8_unicode_ci;; select * from lang where dt='1979-12-09';`
  * [Revision #3077.188.73](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.73) \[merge]\
    Mon 2013-07-01 15:38:16 +0200
    * merge 5.1 => 5.5
    * [Revision #2661.848.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.48)\
      Mon 2013-07-01 15:30:55 +0200
      * Bug#58165: "my\_empty\_string" gets modified and causes LOAD DATA to fail and Cleanup test case (left outfile in data dir)
  * [Revision #3077.188.72](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.72)\
    Mon 2013-07-01 16:53:30 +0530
  * [Revision #3077.188.71](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.71) \[merge]\
    Fri 2013-06-28 17:13:44 +0300
    * merge back to the 5.5 tree and fix indentation
    * [Revision #3077.189.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.189.1)\
      Wed 2013-06-26 12:19:02 +0300
      * Bug #16996656: UNIQUE OPTION PREFIXES NOT DEPRECATED IN 5.5+
  * [Revision #3077.188.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.70)\
    Fri 2013-06-28 13:18:16 +0200
    * Bug#16589511: MYSQL\_UPGRADE FAILS TO WRITE OUT ENTIRE ALTER TABLE ... ALGORITHM= ... STATEMENT
  * [Revision #3077.188.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.69)\
    Thu 2013-06-27 10:08:30 +0200
    * Updated copyright year in the spec file
  * [Revision #3077.188.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.68)\
    Thu 2013-06-27 09:18:48 +0200\
    \*
    * Spec file cleanup for 5.5.33 release to resolve rpm dependencies bugs
  * [Revision #3077.188.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.67)\
    Wed 2013-06-26 11:43:44 +0200
    * Cleaned up spec file for 5.5.33 release
  * [Revision #3077.188.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.66)\
    Wed 2013-06-26 10:02:42 +0530
    * Bug #16994338 PARSING TAP OUTPUT OF UNIT TEST EXPLAIN\_FILENAME-T FAILS
  * [Revision #3077.188.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.65)\
    Tue 2013-06-25 09:42:54 +0800
    * Bug 16876388 - PLEASE BACKPORT BUG#16208542 TO 5.5
  * [Revision #3077.188.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.64)\
    Mon 2013-06-24 13:56:11 +0300
  * [Revision #3077.188.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.63)\
    Mon 2013-06-24 11:11:55 +0530
    * Bug#16753869:INCORRECT TRUNCATION OF LONG SET EXPRESSION IN LOAD DATA CAN CAUSE SQL INJECTION
  * [Revision #3077.188.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.62)\
    Mon 2013-06-24 10:42:40 +0530
  * [Revision #3077.188.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.61)\
    Fri 2013-06-21 14:18:01 +0200
    * Bug#16945503 ADDRESSSANITIZER BUG IN SYS\_VARS Sys\_var\_keycache inherits from some variant of Sys\_var\_integer
  * [Revision #3077.188.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.60) \[merge]\
    Wed 2013-06-19 14:55:46 +0530
    * Bug#11829813 UNUSED MUTEX COMMIT\_THREADS\_M
    * [Revision #2661.848.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.47)\
      Wed 2013-06-19 14:43:15 +0530
      * Bug#11829813 UNUSED MUTEX COMMIT\_THREADS\_M
  * [Revision #3077.188.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.59)\
    Tue 2013-06-18 17:12:28 +0300
    * Fix Bug#16907783 5.5 STILL CRASHES IN DICT\_UPDATE\_STATISTICS WITH CONCURRENT DDL AND I\_S QUERIES
  * [Revision #3077.188.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.58) \[merge]\
    Tue 2013-06-18 15:49:13 +0530
    * [Revision #2661.848.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.46)\
      Tue 2013-06-18 15:48:00 +0530
  * [Revision #3077.188.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.57)\
    Tue 2013-06-18 10:20:30 +0530
  * [Revision #3077.188.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.56)\
    Mon 2013-06-17 10:49:53 +0800
  * [Revision #3077.188.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.55)\
    Fri 2013-06-14 13:33:37 -0500
    * Bug#16914007-INNODB: CHECK TABLE SHOULD MARK AN INDEX AS CORRUPTED IF IT HAS A WRONG COUNT
  * [Revision #3077.188.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.54)\
    Fri 2013-06-14 16:38:27 +0200
    * Bug#14834378 ADDRESSSANITIZER BUG IN FILENAME\_TO\_TABLENAME Backport to 5.5
  * [Revision #3077.188.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.53)\
    Fri 2013-06-14 10:52:23 +0200
    * Bug#16729109: FIX COMPILATION WARNINGS WITH GCC 4.8 Backport to 5.5 (external Bug#69407 Build warnings with mysql)
  * [Revision #3077.188.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.52) \[merge]\
    Fri 2013-06-14 16:55:37 +0530
    * [Revision #2661.848.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.45)\
      Fri 2013-06-14 16:44:49 +0530
  * [Revision #3077.188.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.51) \[merge]\
    Fri 2013-06-14 11:28:29 +0530
    * Bug#13548704 ALGORITHM USED FOR DROPPING PARTITIONED TABLE CAN LEAD TO INCONSISTENCY \[Merge from 5.1]
    * [Revision #2661.848.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.44)\
      Fri 2013-06-14 11:22:05 +0530
      * Bug#13548704 ALGORITHM USED FOR DROPPING PARTITIONED TABLE CAN LEAD TO INCONSISTENCY
  * [Revision #3077.188.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.50)\
    Thu 2013-06-13 11:14:13 +0530
    * Bug #16417635 INNODB FAILS TO MERGE UNDER-FILLED PAGES DEPENDING ON DELETION ORDER
  * [Revision #3077.188.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.49)\
    Wed 2013-06-12 09:35:33 +0200
    * Bug #14227431: CHARACTER SET MISMATCH WHEN ALTERING FOREIGN KEYS CAN LEAD TO MISSING TABLES
  * [Revision #3077.188.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.48)\
    Wed 2013-06-12 12:00:44 +0530
  * [Revision #3077.188.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.47)\
    Mon 2013-06-10 22:29:41 +0200
    * Fixing the bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
  * [Revision #3077.188.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.46) \[merge]\
    Tue 2013-06-11 01:20:25 +0530
    * Upmerging the changes from 5.1 for the bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
    * [Revision #2661.848.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.43)\
      Tue 2013-06-11 01:13:07 +0530
      * Bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
  * [Revision #3077.188.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.45)\
    Fri 2013-06-07 21:34:34 +0200
    * Bug #16917425 -DBUILD\_CONFIG=MYSQL\_RELEASE -DWITH\_DEBUG=ON FAILS 4 AND SKIPS 27 MTR TESTS
  * [Revision #3077.188.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.44)\
    Fri 2013-06-07 19:29:56 +0530
    * Bug #16917425 -DBUILD\_CONFIG=MYSQL\_RELEASE -DWITH\_DEBUG=ON FAILS 4 AND SKIPS 27 MTR TESTS
  * [Revision #3077.188.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.43) \[merge]\
    Thu 2013-06-06 15:47:55 +0200
    * Null merging the changes of 5.1 branch
    * [Revision #2661.848.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.42) \[merge]\
      Tue 2013-06-04 18:17:58 +0200
      * Merge from mysql-5.1.70-release
      * [Revision #2661.852.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.852.5)\
        Mon 2013-05-13 15:26:11 +0200
      * [Revision #2661.852.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.852.4)\
        Mon 2013-05-13 15:22:49 +0200
        * Merging the changes for build failures in windows.
      * [Revision #2661.852.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.852.3)\
        Fri 2013-05-10 15:27:03 +0200
        * Merging the changes which fixes the build issue for Windows Builds. Description: Fixing a build issue. The function innobase\_convert\_to\_system\_charset() is included only in the builtin InnoDB, and it is missed in InnoDB plugin. Adding this function in InnoDB plugin as well.
      * [Revision #2661.852.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.852.2)\
        Tue 2013-05-07 09:14:51 +0200
        * Updated spec file to ignore upgrade error message
      * [Revision #2661.852.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.852.1)\
        Tue 2013-05-07 08:10:09 +0200
        * Merging the changes from 5.1 branch to release branch. Includes bug fixes for: Bug #16722314 FOREIGN KEY ID MODIFIED DURING EXPORT Bug #16754901 PARS\_INFO\_FREE NOT CALLED IN DICT\_CREATE\_ADD\_FOREIGN\_TO\_DICTIONARY
  * [Revision #3077.188.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.42) \[merge]\
    Wed 2013-06-05 14:17:01 +0200
    * Merge from mysql-5.5.32-release
  * [Revision #3077.188.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.41)\
    Mon 2013-06-03 16:34:43 +0530
    * BUG #13619394 - MAKE TEST FAILS ON MY\_VSNPRINTF
  * [Revision #3077.188.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.40)\
    Wed 2013-05-29 20:09:45 +0530
    * Fix to remove unreferenced components
  * [Revision #3077.188.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.39)\
    Fri 2013-05-24 18:17:36 +0200
    * 4371 Maitrayi Sabaratnam 2013-05-23 Bug#13116514 - CREATE LOGFILE GROUP INITIAL\_SIZE & UNDO\_BUFFER\_SIZE FAILS
  * [Revision #3077.188.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.38)\
    Fri 2013-05-24 13:58:42 +0300
    * Bug#16859867 INNODB\_BUG14529666 FAILS SPORADICALLY IN VALGRIND
  * [Revision #3077.188.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.37) \[merge]\
    Fri 2013-05-24 14:35:00 +0530
    * Bug#16765278 DELETE SQL\_LOAD\_MB\* FILE (TEMP FILE) CREATED BY BINLOG\_KILLED\_SIMULATE.TEST Merging fix from mysql-5.1
    * [Revision #2661.848.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.41)\
      Fri 2013-05-24 14:25:00 +0530
      * Bug#16765278 DELETE SQL\_LOAD\_MB\* FILE (TEMP FILE) CREATED BY BINLOG\_KILLED\_SIMULATE.TEST
  * [Revision #3077.188.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.36) \[merge]\
    Thu 2013-05-23 15:02:33 +0530
    * Null merge from 5.1 to 5.5
    * [Revision #2661.848.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.40)\
      Thu 2013-05-23 15:00:31 +0530
      * Bug #16119355: PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
  * [Revision #3077.188.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.35) \[merge]\
    Thu 2013-05-23 11:06:34 +0530
    * Merge from 5.5 to 5.6
    * [Revision #2661.848.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.39)\
      Wed 2013-05-22 14:36:43 +0530
      * Bug#11766191:INVALID MEMORY READ IN DO\_DIV\_MOD WITH DOUBLY ASSIGNED VARIABLES Bug#12608543: CRASHES WITH DECIMALS AND STATEMENT NEEDS TO BE REPREPARED ERRORS
  * [Revision #3077.188.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.34)\
    Mon 2013-05-20 14:00:40 +0530
  * [Revision #3077.188.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.33)\
    Sun 2013-05-19 23:38:06 +0530
    * Bug#16194302: SUPPORT FOR FLOATING-POINT SYSTEM VARIABLES USING THE PLUGIN INTERFACE.
  * [Revision #3077.188.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.32)\
    Sat 2013-05-18 10:20:56 +0530
    * Bug #12762377 FOREIGN KEYS NOT CONSTRUCTED WHEN APOSTROPHES ARE ESCAPED WITH BACKSLASH
  * [Revision #3077.188.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.31)\
    Fri 2013-05-17 18:54:36 +0530
    * Bug#14236170 MYSQLDUMP 5.5.25 CLIENT FAILS TO DUMP MYSQL DB FROM REMOTE 5.0.96 SERVER
  * [Revision #3077.188.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.30)\
    Fri 2013-05-17 08:00:38 +0530
  * [Revision #3077.188.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.29)\
    Thu 2013-05-16 18:14:25 +0530
    * BUG #16813006 - UNIT TEST FOR MY\_VSNPRINTF FAIL FOR NON GNU COMPILER
  * [Revision #3077.188.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.28)\
    Thu 2013-05-16 11:02:39 +0200
    * Bug#16447483: PARTITION PRUNING IS NOT CORRECT FOR RANGE COLUMNS
  * [Revision #3077.188.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.27)\
    Thu 2013-05-16 16:56:02 +0530
    * Fixing a compiler warning issue. At the end of the function ibuf\_insert\_to\_index\_page\_low() add a DBUG\_RETURN(NULL).
  * [Revision #3077.188.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.26) \[merge]\
    Thu 2013-05-16 14:34:06 +0530
    * Bug 16813007 5.1 => 5.5 null
    * [Revision #2661.848.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.38)\
      Thu 2013-05-16 14:32:09 +0530
      * Bug #16813007 - MTR IS NOT TAKING MYSQLTEST CLIENT USING THE ENV VARIABLE MYSQL\_TEST
  * [Revision #3077.188.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.25) \[merge]\
    Thu 2013-05-16 14:19:57 +0530
    * Bug 16813007 5.1 => 5.5
    * [Revision #2661.851.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.851.1)\
      Thu 2013-05-16 14:18:04 +0530
      * Bug #16813007 - MTR IS NOT TAKING MYSQLTEST CLIENT USING THE ENV VARIABLE MYSQL\_TEST
  * [Revision #3077.188.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.24) \[merge]\
    Thu 2013-05-16 14:05:51 +0530
    * Null merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.37)\
      Thu 2013-05-16 14:05:05 +0530
      * Bug #16806366 BOGUS CALL TO LOCK\_REC\_RESTORE\_FROM\_PAGE\_INFIMUM IN INSERT BUFFER MERGE
  * [Revision #3077.188.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.23) \[merge]\
    Thu 2013-05-16 13:58:26 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.850.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.850.1)\
      Thu 2013-05-16 10:26:09 +0530
      * Bug #16806366 BOGUS CALL TO LOCK\_REC\_RESTORE\_FROM\_PAGE\_INFIMUM IN INSERT BUFFER MERGE
  * [Revision #3077.188.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.22) \[merge]\
    Thu 2013-05-16 09:01:11 +0200
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.36)\
      Thu 2013-05-16 08:09:48 +0200
      * Bug#16807394: PREVENT NEW ERROR MESSAGES FROM BEING ADDED TO 5.5
  * [Revision #3077.188.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.21)\
    Thu 2013-05-16 13:34:50 +0800
  * [Revision #3077.188.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.20)\
    Thu 2013-05-16 10:01:06 +0530
    * Bug #16411457 MASTER THREAD CANNOT EXIT FLUSH\_LOOP WHEN INNODB\_FAST\_SHUTDOWN IS 2
  * [Revision #3077.188.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.19) \[merge]\
    Wed 2013-05-15 22:50:44 +0300
    * Merge mysql-5.1 to mysql-5.5.
    * [Revision #2661.848.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.35)\
      Wed 2013-05-15 22:40:29 +0300
      * Bug#16736929 PAGE\_ZIP\_DECOMPRESS() FAILS ON EMPTY RECORD
  * [Revision #3077.188.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.18)\
    Wed 2013-05-15 10:47:19 -0400
    * Bug#16622478 INNODB'S THREAD CONCURRENCY TICKETS MIGHT BE RELEASED AFTER A ROW IS READ
  * [Revision #3077.188.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.17)\
    Wed 2013-05-15 07:59:01 +0200
  * [Revision #3077.188.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.16)\
    Tue 2013-05-14 22:52:42 +0530
    * Bug#16607258 :Linker Errors Due To Inclusion Of An Implementation File In log\_event.h
  * [Revision #3077.188.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.15)\
    Mon 2013-05-13 22:05:56 +0800
    * Bug#14529666 INNODB\_BUFFER\_PAGE DOES NOT MARK CHANGE BUFFER PAGES APPROPRIATELY
  * [Revision #3077.188.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.14)\
    Mon 2013-05-13 17:15:25 +0530
    * Bug#12328597 - MULTIPLE COUNT(DISTINCT) IN SAME SELECT FALSE WITH COMPOSITE KEY COLUMNS
  * [Revision #3077.188.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.13) \[merge]\
    Mon 2013-05-13 12:27:33 +0530
    * Null merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.34)\
      Mon 2013-05-13 12:01:17 +0530
  * [Revision #3077.188.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.12) \[merge]\
    Sun 2013-05-12 19:45:42 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.33)\
      Sun 2013-05-12 19:41:25 +0530
      * Fixing a build issue. In InnoDB plugin, the function innobase\_convert\_to\_filename\_charset() was by mistake kept within the conditional compilation of UNIV\_COMPILE\_TEST\_FUNCS. Now placing the function out of UNIV\_COMPILE\_TEST\_FUNCS. Also, removed the unnecessary log message (as in 5.6+).
  * [Revision #3077.188.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.11) \[merge]\
    Fri 2013-05-10 19:21:40 +0530
    * Null merge from 5.1 to 5.5
    * [Revision #2661.848.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.32)\
      Fri 2013-05-10 19:18:21 +0530
      * Bug#16119355:PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
  * [Revision #3077.188.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.10) \[merge]\
    Fri 2013-05-10 15:38:25 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.31)\
      Fri 2013-05-10 15:35:40 +0530
      * Fixing a build issue. The function innobase\_convert\_to\_system\_charset() is included only in the builtin InnoDB, and it is missed in InnoDB plugin. Adding this function in InnoDB plugin as well.
  * [Revision #3077.188.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.9)\
    Thu 2013-05-09 14:01:51 +0530
  * [Revision #3077.188.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.8)\
    Wed 2013-05-08 12:52:12 +0200
    * Bug#16779374: NEW ERROR MESSAGE ADDED TO 5.5 AFTER 5.6 GA - REUSING NUMBER ALREADY USED BY 5.6
  * [Revision #3077.188.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.7) \[merge]\
    Tue 2013-05-07 18:00:00 +0530
    * Merge from 5.1 to 5.5
    * [Revision #2661.848.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.30)\
      Tue 2013-05-07 16:08:48 +0530
      * Bug #16119355: PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
  * [Revision #3077.188.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.6) \[merge]\
    Tue 2013-05-07 13:14:01 +0400
    * 5.1 -> 5.5 merge
    * [Revision #2661.848.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.29)\
      Tue 2013-05-07 13:10:58 +0400
      * Bug#16095534 CRASH: PREPARED STATEMENT CRASHES IN ITEM\_BOOL\_FUNC2::FIX\_LENGTH\_AND\_DEC The problem happened due to broken left expression in Item\_in\_optimizer object. In case of the bug left expression is runtime created Item\_outer\_ref item which is deleted at the end of the statement and one of Item\_in\_optimizer arguments becomes bad when re-executed. The fix is to use real\_item() instead of original left expression. Note: It feels a bit weird that after preparing, the field is directly part of the generated Item\_func\_eq, whereas in execution it is replaced with an Item\_outer\_ref wrapper object.
  * [Revision #3077.188.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.5)\
    Tue 2013-05-07 13:30:25 +0530
    * Bug#16513588:"PREPARE\_COMMIT\_MUTEX" IS NOT FREED DURING TRANSACTION ROLLBACK
  * [Revision #3077.188.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.4) \[merge]\
    Mon 2013-05-06 19:57:49 +0530
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.28)\
      Mon 2013-05-06 16:28:56 +0530
      * Bug #16722314 FOREIGN KEY ID MODIFIED DURING EXPORT Bug #16754901 PARS\_INFO\_FREE NOT CALLED IN DICT\_CREATE\_ADD\_FOREIGN\_TO\_DICTIONARY
  * [Revision #3077.188.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.3)\
    Mon 2013-05-06 15:01:57 +0200
    * Bug#16757869: INNODB: POSSIBLE REGRESSION IN 5.5.31, BUG#16004999
  * [Revision #3077.188.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.2) \[merge]\
    Mon 2013-05-06 10:56:48 +0200
    * Empty version change upmerge
    * [Revision #2661.848.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.27)\
      Mon 2013-05-06 10:25:03 +0200
      * Raise version number after cloning 5.1.70
  * [Revision #3077.188.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.1)\
    Mon 2013-05-06 09:51:25 +0200
    * Raise version number after cloning 5.5.32
* [Revision #3879](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3879) \[merge]\
  Fri 2013-09-06 10:34:38 -0700
  * Merge 5.3->5.5
  * [Revision #2502.567.132](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.132)\
    Fri 2013-09-06 09:55:32 -0700
    * Fixed bug [MDEV-4996](https://jira.mariadb.org/browse/MDEV-4996). The fix for bug [MDEV-4971](https://jira.mariadb.org/browse/MDEV-4971) not always correctly set the pointers to inherited multiple equalities in objects of the Item\_equal class.
* [Revision #3878](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3878)\
  Fri 2013-09-06 15:59:19 +0400
  * [MDEV-4978](https://jira.mariadb.org/browse/MDEV-4978) - Server cursor is broken with blobs in the select list, ORDER BY does not work
* [Revision #3877](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3877)\
  Tue 2013-09-03 22:45:12 +0200
  * [MDEV-4926](https://jira.mariadb.org/browse/MDEV-4926): Remove division-using-subtraction implementation from semi-sync plugin
* [Revision #3876](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3876) \[merge]\
  Tue 2013-09-03 18:41:07 +0400
  * [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Merge into 5.5-main
  * [Revision #3864.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3864.1.2)\
    Wed 2013-08-28 21:21:12 +0400
    * [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942): Add another testcase after merging with other fixes.
  * [Revision #3864.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3864.1.1) \[merge]\
    Wed 2013-08-28 20:31:23 +0400
    * Automatic merge of [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836) fix into 5.5
    * [Revision #3861.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3861.1.2)\
      Mon 2013-08-26 21:38:04 +0400
      * Fix for [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836) fix: take into account situation where "notnull\_col IS NULL" is not a direct child of the WHERE clause item, but rather is embedded inside Item\_cond\_and or Item\_cond\_or.
    * [Revision #3861.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3861.1.1) \[merge]\
      Mon 2013-08-26 16:31:58 +0400
      * Fix for [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Merge with current 5.5
      * [Revision #3858.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3858.1.1)\
        Fri 2013-08-23 16:32:56 +0400
        * [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Wrong result on IS NULL (old documented hack stopped working) - When applying optimization introduced by [MDEV-4817](https://jira.mariadb.org/browse/MDEV-4817), ignore the conditions that have form "datetime\_not\_null\_col IS NULL".
* [Revision #3875](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3875) \[merge]\
  Sat 2013-08-31 09:33:09 -0700
  * Merge
  * [Revision #3873.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3873.1.1) \[merge]\
    Sat 2013-08-31 08:18:25 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.131](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.131)\
      Thu 2013-08-29 21:02:42 -0700
      * Fixed bug [MDEV-4971](https://jira.mariadb.org/browse/MDEV-4971). The function propagate\_new\_equalities() did not updated properly the references to inherited multiple equalities.
* [Revision #3874](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3874)\
  Fri 2013-08-30 11:00:29 +0400
  * [MDEV-4902](https://jira.mariadb.org/browse/MDEV-4902) - sql\_yacc.yy incompatible with bison 3
* [Revision #3873](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3873) \[merge]\
  Thu 2013-08-29 12:32:09 -0700
  * Merge 5.3->5.5
  * [Revision #2502.567.130](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.130)\
    Thu 2013-08-29 10:56:12 -0700
    * Fixed bug [MDEV-4962](https://jira.mariadb.org/browse/MDEV-4962). When a non-nullable datetime field is used under an IS NULL predicate of the WHERE condition in a query with outer joins the remove\_eq\_conds function should check whether this field belongs to an inner table of any outer join that can be, in a general case, a nested outer join.
* [Revision #3872](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3872)\
  Wed 2013-08-28 22:16:13 +0200
  * fix an old bug where dd\_frm\_type() could incorrectly determine the table type for dynamic engines (because it only looked at the one-byte code, not at the full engine name).
* [Revision #3871](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3871)\
  Wed 2013-08-28 22:16:03 +0200
  * Test case for MyISAM and OPTIMIZE TABLE that requires MDL\_SHARED\_NO\_READ\_WRITE.
* [Revision #3870](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3870)\
  Mon 2013-08-26 21:14:34 +0400
  * bugfix: storage engine might return a negative error code, but it shouldn't be ignored on return
* [Revision #3869](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3869)\
  Mon 2013-08-26 21:14:01 +0400
  * mtr bug: files outside of both the suite dir and the overlay dir, were treated as coming from the overlay.
* [Revision #3868](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3868)\
  Mon 2013-08-26 21:13:17 +0400
  * don't decide on extended keys by DB\_TYPE\_INNODB, use hton->flags
* [Revision #3867](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3867)\
  Mon 2013-08-26 21:04:10 +0400
  * HA\_ERR\_TABLE\_DEF\_CHANGED is normal situation, not an server-wide exception, don't log it to the error log.
* [Revision #3866](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3866)\
  Mon 2013-08-26 21:03:01 +0400
  * typo fixed (boolean index attributes didn't work)
* [Revision #3865](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3865)\
  Wed 2013-08-28 07:49:53 +0200
  * [MDEV-4951](https://jira.mariadb.org/browse/MDEV-4951) drop user leaves privileges
* [Revision #3864](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3864)\
  Wed 2013-08-28 09:14:57 -0700
  * Fixed bug [MDEV-4959](https://jira.mariadb.org/browse/MDEV-4959). The fix for [MDEV-4420](https://jira.mariadb.org/browse/MDEV-4420) was not quite correct. This patch corrects it.
* [Revision #3863](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3863) \[merge]\
  Tue 2013-08-27 22:19:14 -0700
  * Merge 5.3->5.5
  * [Revision #2502.567.129](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.129)\
    Mon 2013-08-26 15:51:47 -0700
    * Fixed bug [MDEV-4952](https://jira.mariadb.org/browse/MDEV-4952) When in function remove\_eq\_conds() a sub-formula of the processed condition is replaced for another formula we should ensure that in the resulting formula AND/OR levels must alternate.
  * [Revision #2502.567.128](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.128)\
    Mon 2013-08-26 12:55:58 -0700
    * Fixed bug [MDEV-4944](https://jira.mariadb.org/browse/MDEV-4944). The patch to fix [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) turned out to be incorrect. At the substitution of single row tables in make\_join\_statistics() the used multiple equalities may change and references to the new multiple equalities must be updated. The function remove\_eq\_conds() takes care of it and it should be called right after the substitution of single row tables. Calling it after the call of make\_join\_statistics was a mistake.
* [Revision #3862](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3862)\
  Tue 2013-08-27 19:18:04 +0300
  * Fixed MySQL bug #69861 LAST\_INSERT\_ID is replicated incorrectly if replication filters are used
* [Revision #3861](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3861) \[merge]\
  Mon 2013-08-26 16:23:14 +0400
  * Merge fix for [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942), 5.3->5.5
  * [Revision #2502.567.127](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.127)\
    Fri 2013-08-23 22:17:02 -0700
    * Fixed bug [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942). Made sure that degenerate conjunctions/disjunctions are obtained from AND/OR conditions.
* [Revision #3860](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3860) \[merge]\
  Fri 2013-08-23 08:34:35 -0700
  * Merge
  * [Revision #3857.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3857.1.1)\
    Fri 2013-08-23 07:25:45 -0700
    * Fixed bug [MDEV-4420](https://jira.mariadb.org/browse/MDEV-4420). The code of JOIN::optimize that performed substitutions for the best equal field in all ref items did not take into account that a multiple equality could contain the result of the single-value subquery if the subquery is inexpensive. This code was corrected. Also made necessary corresponding corrections in the code of make\_join\_select().
* [Revision #3859](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3859) \[merge]\
  Thu 2013-08-22 16:23:54 +0400
  * Merging from 5.3
  * [Revision #2502.567.126](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.126)\
    Thu 2013-08-22 15:20:27 +0400
    * [MDEV-4804](https://jira.mariadb.org/browse/MDEV-4804) Date comparing false result
* [Revision #3858](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3858) \[merge]\
  Thu 2013-08-22 14:13:46 +0400
  * Automatic merge
  * [Revision #3855.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3855.1.1)\
    Thu 2013-08-22 14:12:10 +0400
    * [MDEV-4840](https://jira.mariadb.org/browse/MDEV-4840): Wrong result (missing rows) on LEFT JOIN with InnoDB tables Fix two problems in table elimination code: - Before marking a "value" as bound, check if it is already bound. Marking the same value as bound twice could confuse a module that depends on this value, because Dep\_module\_XXX use counters to know when they become bound.
* [Revision #3857](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3857) \[merge]\
  Wed 2013-08-21 12:34:58 -0700
  * Merge
  * [Revision #2502.567.125](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.125)\
    Wed 2013-08-21 17:42:09 +0300
    * [MDEV-4908](https://jira.mariadb.org/browse/MDEV-4908): Assertion \`((Item\_cond \*) cond)->functype() == ((Item\_cond \*) new\_item)->functype()' fails on a query with IN and equal conditions, AND/OR, materialization+semijoin
* [Revision #3856](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3856) \[merge]\
  Wed 2013-08-21 11:27:02 -0700
  * Merge 5.3->5.5
  * [Revision #2502.567.124](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.124)\
    Tue 2013-08-20 13:47:13 -0700
    * Fixed a bug/typo in the patch for [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355), noticed after the patch had been merged into 5.5.
  * [Revision #2502.567.123](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.123)\
    Tue 2013-08-20 17:08:03 +0300
    * Fix bug [MDEV-4895](https://jira.mariadb.org/browse/MDEV-4895) Valgrind warnings (Conditional jump or move depends on uninitialised value) in Field\_datetime::get\_date on GREATEST(..) IS NULL
  * [Revision #2502.567.122](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.122)\
    Mon 2013-08-19 14:24:48 -0700
    * Backported from maria-5.5 the fix in the patch for [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) that had been discovered when merging the patch from 5.3 into 5.5.
* [Revision #3855](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3855)\
  Tue 2013-08-20 16:05:34 +0300
  * [MDEV-4923](https://jira.mariadb.org/browse/MDEV-4923) Incorrect merge on XtraDB os0file.c. Function os\_file\_set\_atomic\_writes returns TRUE when successfull and FALSE at failure.
* [Revision #3854](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3854)\
  Tue 2013-08-20 10:42:38 +0200
  * Backport from 10.0-base fix for tests failing when vardir has no execute permissions.
* [Revision #3853](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3853) \[merge]\
  Mon 2013-08-19 08:55:49 -0700
  * Merge
  * [Revision #3850.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3850.1.2) \[merge]\
    Sun 2013-08-18 22:13:49 -0700
    * Merge
  * [Revision #3850.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3850.1.1) \[merge]\
    Sun 2013-08-18 19:58:51 -0700
    * Merge 5.3->5.5. In particular: Merged the patch for bug [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) from 5.3 into 5.5. Fixed a bug in the patch that should be backported to 5.3.
    * [Revision #2502.567.121](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.121)\
      Fri 2013-08-16 22:01:47 -0700
      * Fixed bug [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418). After single row substitutions there might appear new equalities. They should be properly propagated to all AND/OR levels the WHERE condition. It's done now with an additional call of remove\_eq\_conds().
    * [Revision #2502.567.120](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.120) \[merge]\
      Thu 2013-08-15 16:59:20 -0700
      * Merge
      * [Revision #2502.578.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.578.1)\
        Thu 2013-08-15 14:16:16 -0700
        * Fixed bug [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355). This patch almost totally revised the patch for bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177). The latter had too many defects. In particular, it did not propagate multiple equalities formed when merging a degenerate disjunct into underlying AND formula.
    * [Revision #2502.567.119](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.119) \[merge]\
      Thu 2013-08-15 14:04:20 -0700
      * Merge 5.2->5.3
      * [Revision #2502.566.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.53) \[merge]\
        Wed 2013-08-14 20:37:38 -0700
        * Merge 5.1->5.2
        * [Revision #2502.565.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.53)\
          Tue 2013-08-13 15:21:11 -0700
          * Fixed bug [MDEV-4894](https://jira.mariadb.org/browse/MDEV-4894). This a an old legacy performance bug. When a very selective range scan existed for the second table in a join, and, at the same time, there was another range condition depending on the fields of the first table, the optimizer chose a plan with 'Range checked for each record'. This plan was extremely inefficient in comparison with the regular selective range scan. As a matter of fact the range scan chosen for each record was the same as that selective range scan.
        * [Revision #2502.565.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.52)\
          Mon 2013-07-22 00:55:06 +0500
          * [MDEV-4478](https://jira.mariadb.org/browse/MDEV-4478) check mysql-5.5 changes in spatial.cc. not\_enough\_points() introduced to check if the spatial object is incorrect.
      * [Revision #2502.566.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.52)\
        Thu 2013-08-01 09:25:50 +0300
        * [MDEV-4823](https://jira.mariadb.org/browse/MDEV-4823): Server crashes in Item\_func\_not::fix\_fields on creating a table with a virtual column using NOT
* [Revision #3852](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3852)\
  Sat 2013-08-17 17:20:09 +0400
  * [MDEV-4165](https://jira.mariadb.org/browse/MDEV-4165) \[PATCH] RFE: make tmpdir a build-time configurable option
* [Revision #3851](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3851)\
  Wed 2013-08-14 11:12:57 +0200
  * fix a comment
* [Revision #3850](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3850) \[merge]\
  Mon 2013-08-12 17:33:08 +0400
  * Merge from 5.3
  * [Revision #2502.567.118](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.118)\
    Mon 2013-08-12 16:47:59 +0400
    * [MDEV-4652](https://jira.mariadb.org/browse/MDEV-4652) Wrong result for CONCAT(GREATEST(TIME('00:00:01'),TIME('00:00:00'))
  * [Revision #2502.567.117](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.117)\
    Thu 2013-08-01 11:46:11 +0300
    * [MDEV-4811](https://jira.mariadb.org/browse/MDEV-4811) Assertion \`offset < 0x1f' fails in type\_and\_offset\_store on COLUMN\_ADD [MDEV-4812](https://jira.mariadb.org/browse/MDEV-4812) Valgrind warnings (Invalid write) in dynamic\_column\_update\_many on COLUMN\_ADD
* [Revision #3849](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3849)\
  Thu 2013-08-08 13:33:15 +0200
  * mysql `--skip-column-names` flag should not affect alignment of field values, set num\_flag\[] unconditionally, not under "if (column\_names)"
* [Revision #3848](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3848) \[merge]\
  Thu 2013-08-08 13:41:21 +0400
  * Merge from 5.3
  * [Revision #2502.567.116](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.116)\
    Thu 2013-08-08 12:58:28 +0400
    * [MDEV-4653](https://jira.mariadb.org/browse/MDEV-4653) Wrong result for CONVERT\_TZ(TIME('00:00:00'),'+00:00','+7:5')
* [Revision #3847](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3847) \[merge]\
  Thu 2013-08-08 11:48:49 +0400
  * Merge from 5.3
  * [Revision #2502.567.115](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.115)\
    Thu 2013-08-08 11:36:03 +0400
    * [MDEV-4512](https://jira.mariadb.org/browse/MDEV-4512) Valgrind warnings in my\_long10\_to\_str\_8bit on INTERVAL and DATE\_ADD with incorrect types Fixing a typo: bit AND (&) was erroneously used instead of logical AND (&&)
* [Revision #3846](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3846)\
  Mon 2013-08-05 17:34:38 +0300
  * Fix possible race condition in Query cache.
* [Revision #3845](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3845) \[merge]\
  Mon 2013-08-05 20:59:15 +0400
  * Automatic merge
  * [Revision #3843.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3843.2.1)\
    Mon 2013-08-05 20:57:48 +0400
    * Update test results after fix for [MDEV-4687](https://jira.mariadb.org/browse/MDEV-4687)
* [Revision #3844](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3844) \[merge]\
  Mon 2013-08-05 21:21:21 +0400
  * Fixes for storage\_engine tests diverged from the main line
  * [Revision #3843.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3843.1.3)\
    Mon 2013-08-05 20:31:29 +0400
    * Deliberate change in behavior introduced in MySQL 5.5.31 along with the partitioning enhancement for Bug#14521864
  * [Revision #3843.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3843.1.2)\
    Mon 2013-08-05 18:42:22 +0400
    * The test was non-deterministic while choosing an alternative storage engine
  * [Revision #3843.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3843.1.1)\
    Mon 2013-08-05 18:30:12 +0400
    * Deliberate change in behavior introduced along with the fix for [MDEV-4310](https://jira.mariadb.org/browse/MDEV-4310)
* [Revision #3843](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3843)\
  Wed 2013-07-31 17:24:52 +0400
  * [MDEV-4817](https://jira.mariadb.org/browse/MDEV-4817): Optimizer fails to optimize expression of the form 'FOO' IS NULL - Modify the way Item\_cond::fix\_fields() and Item\_cond::eval\_not\_null\_tables() calculate bitmap for Item\_cond\_or::not\_null\_tables(): if they see a "... OR inexpensive\_const\_false\_item OR ..." then the item can be ignored. - Updated test results. There can be more warnings produced since parts of WHERE are evaluated more times.
* [Revision #3842](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3842) \[merge]\
  Wed 2013-07-31 13:37:01 +0400
  * Automatic merge
  * [Revision #3840.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3840.1.1)\
    Thu 2013-07-25 22:42:26 +0400
    * [MDEV-4687](https://jira.mariadb.org/browse/MDEV-4687): impossible where with < operation, but =-5 return one row - Let \_ma\_record\_pos() set SEARCH\_PART\_KEY when doing a search on a prefix of a \[unique] key. Otherwise, \_ma\_search\_pos() would find the first key equal to search key, and assume it is also the last one, which will make a wrong estimate of key's position.
* [Revision #3841](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3841)\
  Mon 2013-07-29 16:03:41 +0200
  * [MDEV-4815](https://jira.mariadb.org/browse/MDEV-4815) - allow multiple mysql\_server\_init() / mysql\_server\_end() in the same process, for embedded library.
* [Revision #3840](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3840)\
  Fri 2013-07-19 13:21:23 +0300
  * Revert reverted patch (as workaround) to have no problem with ongoing fix.
* [Revision #3839](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3839)\
  Thu 2013-07-18 11:16:18 +0300
  * Fix of using uninitialized variadle.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
