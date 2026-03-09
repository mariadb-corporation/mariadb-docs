# MariaDB Galera 5.5.33a Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.33a) |[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-5533a-release-notes.md) |**Changelog** |[Overview of Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 30 Sep 2013

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-5533a-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3428](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3428)\
  2013-09-29 20:53:10 UTC
  * References [Bug #1232890](https://bugs.launchpad.net/bugs/1232890) - Rows\_log\_event type cast only for row events
* [Revision #3427](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3427)\
  Fri 2013-09-27 22:32:49 +0200
  * revert the change for auto-rpm-packages for plugins. galera tree should only build galera-server package
* [Revision #3426](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3426)\
  Fri 2013-09-27 17:07:44 +0300
  * Fix merge error.
* [Revision #3425](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3425) \[merge]\
  Fri 2013-09-27 13:48:58 +0300
  * mariadb-5.5.33a merge
  * [Revision #3334.48.17](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.17)\
    Thu 2013-09-19 22:24:59 +0200
    * 5.5.33a
  * [Revision #3334.48.16](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.16)\
    Thu 2013-09-19 22:24:39 +0200
    * [MDEV-4979](https://jira.mariadb.org/browse/MDEV-4979) mysqld\_safe section in my.cnf doesn't have mariadb equivalent
  * [Revision #3334.48.15](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.15)\
    Thu 2013-09-19 20:19:17 +0200
    * [MDEV-5035](https://jira.mariadb.org/browse/MDEV-5035) debian package conflict libmariadbclient18 5.5.33+maria-1wheezy vs. mariadb-server-5.3 5.3.12-mariadb122wheezy
  * [Revision #3334.48.14](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.14)\
    Thu 2013-09-19 20:19:10 +0200
    * [MDEV-5021](https://jira.mariadb.org/browse/MDEV-5021) tokudb ft-index libraries are build with -DWITHOUT\_TOKUDB=1
  * [Revision #3334.48.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.13)\
    Thu 2013-09-19 20:19:00 +0200
    * [MDEV-5026](https://jira.mariadb.org/browse/MDEV-5026) cannot use system jemalloc
  * [Revision #3334.48.12](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.12)\
    Wed 2013-09-18 17:25:10 +0200
    * [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) Crash in [MariaDB 5.5.33](../../5.5/5.5.33.md) with .frm from older MariaDB release
  * [Revision #3334.48.11](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.11)\
    Wed 2013-09-18 10:30:23 +0200
    * fix upgrades when mariadb-galera-server-5.5 is installed
  * [Revision #3334.48.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.10)\
    Wed 2013-09-18 09:09:27 +0200
    * [MDEV-5029](https://jira.mariadb.org/browse/MDEV-5029) Crash in [MariaDB 5.5.33](../../5.5/5.5.33.md) with .frm from older MariaDB release
  * [Revision #3334.48.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.9) \[merge]\
    Tue 2013-09-17 20:44:34 +0200
    * merge with 5.5-release
    * [Revision #3334.1.564](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.564)\
      Tue 2013-09-17 17:07:45 +0200
      * mariadb-tokudb-engine deb package is not architecture-independent
  * [Revision #3334.48.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.8)\
    Tue 2013-09-17 17:37:03 +0400
    * Fixed tokudb with ccache build failure.
  * [Revision #3334.48.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.7)\
    Tue 2013-09-17 13:49:49 +0400
    * Fixed jemalloc with ccache build failure.
  * [Revision #3334.48.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.6) \[merge]\
    Mon 2013-09-16 16:05:53 +0400
    * Merge from 5.3
    * [Revision #2502.567.142](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.142)\
      Mon 2013-09-16 16:03:55 +0400
      * backport from 10.0
  * [Revision #3334.48.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.5) \[merge]\
    Mon 2013-09-16 14:08:43 +0400
    * Merge from 5.3
    * [Revision #2502.567.141](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.141)\
      Mon 2013-09-16 14:07:01 +0400
      * [MDEV-4861](https://jira.mariadb.org/browse/MDEV-4861) TIME/DATETIME arithmetics does not preserve INTERVAL precision Adding tests only.
  * [Revision #3334.48.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.4) \[merge]\
    Mon 2013-09-16 13:54:12 +0400
    * Merge from 5.3 pending merges: Alexander Barkov 2013-09-16 [MDEV-4870](https://jira.mariadb.org/browse/MDEV-4870) Wrong values of CASE, COALESCE, IF...
    * [Revision #2502.567.140](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.140)\
      Mon 2013-09-16 13:52:13 +0400
      * [MDEV-4870](https://jira.mariadb.org/browse/MDEV-4870) Wrong values of CASE, COALESCE, IFNULL on a combination of different temporal types
  * [Revision #3334.48.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.3) \[merge]\
    Mon 2013-09-16 13:08:19 +0400
    * Merge from 5.3
    * [Revision #2502.567.139](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.139)\
      Mon 2013-09-16 13:03:49 +0400
      * [MDEV-4869](https://jira.mariadb.org/browse/MDEV-4869) Wrong result of MAKETIME(0, 0, -0.1)
  * [Revision #3334.48.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.2) \[merge]\
    Mon 2013-09-16 10:51:03 +0400
    * Merge from 5.3 pending merges: Alexander Barkov 2013-09-16 [MDEV-4843](https://jira.mariadb.org/browse/MDEV-4843) Wrong data type for TIMESTAMP('200...
    * [Revision #2502.567.138](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.138)\
      Mon 2013-09-16 10:14:41 +0400
      * [MDEV-4843](https://jira.mariadb.org/browse/MDEV-4843) Wrong data type for TIMESTAMP('2001-01-01','10:10:10')
  * [Revision #3334.48.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.48.1) \[merge]\
    Sun 2013-09-15 17:30:53 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.137](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.137)\
      Sun 2013-09-15 12:38:22 -0700
      * Fixed bug [MDEV-5015](https://jira.mariadb.org/browse/MDEV-5015). The patch for [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355) had a defect: the cached values for bitmaps of used tables were not updated when processing degenerate OR formulas.
* [Revision #3424](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3424)\
  Fri 2013-09-27 13:01:14 +0300
  * Updated test results because of new system variables and a new lock variable.
* [Revision #3423](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3423)\
  Thu 2013-09-26 17:51:01 +0300
  * Merged revisions `3916--3921` from lp:codership/codership-mysql/5.5-23
* [Revision #3422](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3422)\
  Thu 2013-09-26 16:43:49 +0300
  * Merge revisions `3907--3914` from lp:codership/codership-mysql/5.5-23
* [Revision #3421](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3421)\
  Thu 2013-09-19 09:21:17 +0200
  * updated test results
* [Revision #3420](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3420)\
  Wed 2013-09-18 20:55:58 +0200
  * fix broken (after merge) galera deb packaging
* [Revision #3419](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3419)\
  Wed 2013-09-18 14:59:51 +0200
  * cmake error on osx
* [Revision #3418](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3418) \[merge]\
  Wed 2013-09-18 12:00:23 +0200
  * mariadb-5.5.33 merge
  * [Revision #3334.1.563](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.563)\
    Mon 2013-09-16 21:21:15 +0200
    * specify deb conflicts correctly
  * [Revision #3334.1.562](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.562)\
    Fri 2013-09-13 23:42:29 +0200
    * fix BUILD/compile-solaris-amd64 to produce working binaries
  * [Revision #3334.1.561](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.561)\
    Fri 2013-09-13 23:42:00 +0200
    * [MDEV-5012](https://jira.mariadb.org/browse/MDEV-5012) Server crashes in Item\_ref::real\_item on EXPLAIN with select subqueries or views, constant table, derived\_merge+derived\_with\_keys
  * [Revision #3334.1.560](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.560) \[merge]\
    Fri 2013-09-13 14:47:40 +0400
    * Null-merge from 5.3.
    * [Revision #2502.567.136](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.136)\
      Fri 2013-09-13 14:43:10 +0400
      * [MDEV-4724](https://jira.mariadb.org/browse/MDEV-4724) Some temporal functions do not preserve microseconds
  * [Revision #3334.1.559](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.559) \[merge]\
    Fri 2013-09-13 13:19:29 +0300
    * merge 5.3->5.5
    * [Revision #2502.567.135](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.135)\
      Thu 2013-09-12 17:05:29 +0300
      * [MDEV-5005](https://jira.mariadb.org/browse/MDEV-5005): Subquery in Procedure somehow affecting temporary table
  * [Revision #3334.1.558](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.558) \[merge]\
    Fri 2013-09-13 12:06:17 +0400
    * Merge from 5.3.
    * [Revision #2502.579.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.579.1)\
      Thu 2013-09-12 21:31:14 +0400
      * [MDEV-4724](https://jira.mariadb.org/browse/MDEV-4724) Some temporal functions do not preserve microseconds
  * [Revision #3334.1.557](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.557) \[merge]\
    Thu 2013-09-12 13:54:46 +0400
    * Merge 5.3 -> 5.5
    * [Revision #2502.567.134](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.134)\
      Thu 2013-09-12 13:53:13 +0400
      * [MDEV-5011](https://jira.mariadb.org/browse/MDEV-5011): ERROR Plugin 'MEMORY' has ref\_count=1 after shutdown for SJM queries - Provide a special execution path for cleanup of degenerate non-merged semi-join children of degenerate selects.
  * [Revision #3334.1.556](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.556)\
    Thu 2013-09-12 10:10:09 +0200
    * tokudb buildbot fixes
  * [Revision #3334.1.555](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.555)\
    Wed 2013-09-11 15:35:49 +0200
    * support ./mtr suite.test,com,bi,na,tions syntax
  * [Revision #3334.1.554](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.554) \[merge]\
    Tue 2013-09-10 23:02:25 +0200
    * merge with 5.5-tokudb tree. In particular:
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
  * [Revision #3334.1.553](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.553)\
    Tue 2013-09-10 11:04:14 +0200
    * fix insert.test in `--ps-protocol`.
  * [Revision #3334.1.552](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.552) \[merge]\
    Tue 2013-09-10 10:08:11 +0400
    * Merge from 5.3
    * [Revision #2502.567.133](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.133)\
      Mon 2013-09-09 15:32:25 +0400
      * [MDEV-4863](https://jira.mariadb.org/browse/MDEV-4863) COALESCE(time\_or\_datetime) returns wrong results in numeric context
  * [Revision #3334.1.551](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.551)\
    Mon 2013-09-09 19:31:29 +0200
    * [MDEV-4941](https://jira.mariadb.org/browse/MDEV-4941) make: AIX fails with 'Identifier not allowed in cast'; syntax error in include/my\_global.h
  * [Revision #3334.1.550](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.550)\
    Mon 2013-09-09 16:56:35 +0500
    * [MDEV-4472](https://jira.mariadb.org/browse/MDEV-4472) Audit-plugin. Server-related part of the task. file\_logger became the service. Data like query\_id now are sent to the audit plugin. Fix for [MDEV-4770](https://jira.mariadb.org/browse/MDEV-4770) ported from 10.0. Fix added for the read\_maria\_plugin\_info(). Log rotation can be disabled with 'set rotations=0'.
  * [Revision #3334.1.549](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.549)\
    Sun 2013-09-08 11:36:34 +0200
    * fix for xtradb to compile on windows
  * [Revision #3334.1.548](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.548)\
    Sat 2013-09-07 22:36:34 +0200
    * fix xtradb to compile in both debug and optimized builds
  * [Revision #3334.1.547](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.547) \[merge]\
    Sat 2013-09-07 13:49:15 +0200
    * Percona-Server-5.5.33-rel31.1.tar.gz
    * [Revision #0.12.64](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/0.12.64)\
      Sat 2013-09-07 09:47:42 +0200
      * Percona-Server-5.5.33-rel31.1.tar.gz
  * [Revision #3334.1.546](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.546) \[merge]\
    Fri 2013-09-06 22:31:30 +0200
    * mysql-5.5.33 merge
    * [Revision #3077.188.78](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.78)\
      Mon 2013-07-15 13:41:27 +0200
      * Removed random passwords feature for Bugfix#17160741 (not applicable for 5.5.X)
    * [Revision #3077.188.77](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.77)\
      Wed 2013-07-10 19:14:41 +0200
      * Updated spec file for Bug#17080138
    * [Revision #3077.188.76](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.76)\
      Tue 2013-07-09 20:35:26 +0200
      * Removed directory /usr/share/mysql/solaris/postinstall-solaris to resolve build error
    * [Revision #3077.188.75](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.75)\
      Fri 2013-07-05 14:30:15 +0530
      * Bug#17033706 SINCE 5.5.32 & 5.6.12, INNODB CANT START WITH OWN MULTI-FILE TABLESPACE
    * [Revision #3077.188.74](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.74)\
      Thu 2013-07-04 16:59:09 +0530
      * Bug #16567381 DATETIME FIELD COMPARISONS DO NOT WORK PROPERLY WITH UTF8\_UNICODE\_CI COLLATION Problem Description: When comparing datetime values with strings, the utf8\_unicode\_ci collation prevents correct comparisons. Consider the below set of queries, it is not showing any results on a table which has tuples that satisfies the query. But for collation utf8\_general\_ci it shows one tuple. `set names utf8 collate utf8_unicode_ci;;` `select * from lang where dt='1979-12-09';`
    * [Revision #3077.188.73](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.73) \[merge]\
      Mon 2013-07-01 15:38:16 +0200
      * merge 5.1 => 5.5
      * [Revision #2661.848.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.48)\
        Mon 2013-07-01 15:30:55 +0200
        * Bug#58165: "my\_empty\_string" gets modified and causes LOAD DATA to fail and Cleanup test case (left outfile in data dir)
    * [Revision #3077.188.72](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.72)\
      Mon 2013-07-01 16:53:30 +0530
    * [Revision #3077.188.71](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.71) \[merge]\
      Fri 2013-06-28 17:13:44 +0300
      * merge back to the 5.5 tree and fix indentation
      * [Revision #3077.189.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.189.1)\
        Wed 2013-06-26 12:19:02 +0300
        * Bug #16996656: UNIQUE OPTION PREFIXES NOT DEPRECATED IN 5.5+
    * [Revision #3077.188.70](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.70)\
      Fri 2013-06-28 13:18:16 +0200
      * Bug#16589511: MYSQL\_UPGRADE FAILS TO WRITE OUT ENTIRE ALTER TABLE ... ALGORITHM= ... STATEMENT
    * [Revision #3077.188.69](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.69)\
      Thu 2013-06-27 10:08:30 +0200
      * Updated copyright year in the spec file
    * [Revision #3077.188.68](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.68)\
      Thu 2013-06-27 09:18:48 +0200\
      \*
      * Spec file cleanup for 5.5.33 release to resolve rpm dependencies bugs
    * [Revision #3077.188.67](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.67)\
      Wed 2013-06-26 11:43:44 +0200
      * Cleaned up spec file for 5.5.33 release
    * [Revision #3077.188.66](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.66)\
      Wed 2013-06-26 10:02:42 +0530
      * Bug #16994338 PARSING TAP OUTPUT OF UNIT TEST EXPLAIN\_FILENAME-T FAILS
    * [Revision #3077.188.65](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.65)\
      Tue 2013-06-25 09:42:54 +0800
      * Bug 16876388 - PLEASE BACKPORT BUG#16208542 TO 5.5
    * [Revision #3077.188.64](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.64)\
      Mon 2013-06-24 13:56:11 +0300
    * [Revision #3077.188.63](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.63)\
      Mon 2013-06-24 11:11:55 +0530
      * Bug#16753869:INCORRECT TRUNCATION OF LONG SET EXPRESSION IN LOAD DATA CAN CAUSE SQL INJECTION
    * [Revision #3077.188.62](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.62)\
      Mon 2013-06-24 10:42:40 +0530
    * [Revision #3077.188.61](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.61)\
      Fri 2013-06-21 14:18:01 +0200
      * Bug#16945503 ADDRESSSANITIZER BUG IN SYS\_VARS Sys\_var\_keycache inherits from some variant of Sys\_var\_integer
    * [Revision #3077.188.60](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.60) \[merge]\
      Wed 2013-06-19 14:55:46 +0530
      * Bug#11829813 UNUSED MUTEX COMMIT\_THREADS\_M
      * [Revision #2661.848.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.47)\
        Wed 2013-06-19 14:43:15 +0530
        * Bug#11829813 UNUSED MUTEX COMMIT\_THREADS\_M
    * [Revision #3077.188.59](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.59)\
      Tue 2013-06-18 17:12:28 +0300
      * Fix Bug#16907783 5.5 STILL CRASHES IN DICT\_UPDATE\_STATISTICS WITH CONCURRENT DDL AND I\_S QUERIES
    * [Revision #3077.188.58](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.58) \[merge]\
      Tue 2013-06-18 15:49:13 +0530
      * [Revision #2661.848.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.46)\
        Tue 2013-06-18 15:48:00 +0530
    * [Revision #3077.188.57](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.57)\
      Tue 2013-06-18 10:20:30 +0530
    * [Revision #3077.188.56](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.56)\
      Mon 2013-06-17 10:49:53 +0800
    * [Revision #3077.188.55](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.55)\
      Fri 2013-06-14 13:33:37 -0500
      * Bug#16914007-INNODB: CHECK TABLE SHOULD MARK AN INDEX AS CORRUPTED IF IT HAS A WRONG COUNT
    * [Revision #3077.188.54](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.54)\
      Fri 2013-06-14 16:38:27 +0200
      * Bug#14834378 ADDRESSSANITIZER BUG IN FILENAME\_TO\_TABLENAME Backport to 5.5
    * [Revision #3077.188.53](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.53)\
      Fri 2013-06-14 10:52:23 +0200
      * Bug#16729109: FIX COMPILATION WARNINGS WITH GCC 4.8 Backport to 5.5 (external Bug#69407 Build warnings with mysql)
    * [Revision #3077.188.52](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.52) \[merge]\
      Fri 2013-06-14 16:55:37 +0530
      * [Revision #2661.848.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.45)\
        Fri 2013-06-14 16:44:49 +0530
    * [Revision #3077.188.51](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.51) \[merge]\
      Fri 2013-06-14 11:28:29 +0530
      * Bug#13548704 ALGORITHM USED FOR DROPPING PARTITIONED TABLE CAN LEAD TO INCONSISTENCY \[Merge from 5.1]
      * [Revision #2661.848.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.44)\
        Fri 2013-06-14 11:22:05 +0530
        * Bug#13548704 ALGORITHM USED FOR DROPPING PARTITIONED TABLE CAN LEAD TO INCONSISTENCY
    * [Revision #3077.188.50](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.50)\
      Thu 2013-06-13 11:14:13 +0530
      * Bug #16417635 INNODB FAILS TO MERGE UNDER-FILLED PAGES DEPENDING ON DELETION ORDER
    * [Revision #3077.188.49](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.49)\
      Wed 2013-06-12 09:35:33 +0200
      * Bug #14227431: CHARACTER SET MISMATCH WHEN ALTERING FOREIGN KEYS CAN LEAD TO MISSING TABLES
    * [Revision #3077.188.48](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.48)\
      Wed 2013-06-12 12:00:44 +0530
    * [Revision #3077.188.47](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.47)\
      Mon 2013-06-10 22:29:41 +0200
      * Fixing the bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
    * [Revision #3077.188.46](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.46) \[merge]\
      Tue 2013-06-11 01:20:25 +0530
      * Upmerging the changes from 5.1 for the bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
      * [Revision #2661.848.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.43)\
        Tue 2013-06-11 01:13:07 +0530
        * Bug 16919882 - WRONG FSF ADDRESS IN LICENSES HEADERS
    * [Revision #3077.188.45](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.45)\
      Fri 2013-06-07 21:34:34 +0200
      * Bug #16917425 -DBUILD\_CONFIG=MYSQL\_RELEASE -DWITH\_DEBUG=ON FAILS 4 AND SKIPS 27 MTR TESTS
    * [Revision #3077.188.44](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.44)\
      Fri 2013-06-07 19:29:56 +0530
      * Bug #16917425 -DBUILD\_CONFIG=MYSQL\_RELEASE -DWITH\_DEBUG=ON FAILS 4 AND SKIPS 27 MTR TESTS
    * [Revision #3077.188.43](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.43) \[merge]\
      Thu 2013-06-06 15:47:55 +0200
      * Null merging the changes of 5.1 branch
      * [Revision #2661.848.42](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.42) \[merge]\
        Tue 2013-06-04 18:17:58 +0200
        * Merge from mysql-5.1.70-release
        * [Revision #2661.852.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.852.5)\
          Mon 2013-05-13 15:26:11 +0200
        * [Revision #2661.852.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.852.4)\
          Mon 2013-05-13 15:22:49 +0200
          * Merging the changes for build failures in windows.
        * [Revision #2661.852.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.852.3)\
          Fri 2013-05-10 15:27:03 +0200
          * Merging the changes which fixes the build issue for Windows Builds. Description: Fixing a build issue. The function innobase\_convert\_to\_system\_charset() is included only in the builtin InnoDB, and it is missed in InnoDB plugin. Adding this function in InnoDB plugin as well.
        * [Revision #2661.852.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.852.2)\
          Tue 2013-05-07 09:14:51 +0200
          * Updated spec file to ignore upgrade error message
        * [Revision #2661.852.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.852.1)\
          Tue 2013-05-07 08:10:09 +0200
          * Merging the changes from 5.1 branch to release branch. Includes bug fixes for: Bug #16722314 FOREIGN KEY ID MODIFIED DURING EXPORT Bug #16754901 PARS\_INFO\_FREE NOT CALLED IN DICT\_CREATE\_ADD\_FOREIGN\_TO\_DICTIONARY
    * [Revision #3077.188.42](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.42) \[merge]\
      Wed 2013-06-05 14:17:01 +0200
      * Merge from mysql-5.5.32-release
    * [Revision #3077.188.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.41)\
      Mon 2013-06-03 16:34:43 +0530
      * BUG #13619394 - MAKE TEST FAILS ON MY\_VSNPRINTF
    * [Revision #3077.188.40](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.40)\
      Wed 2013-05-29 20:09:45 +0530
      * Fix to remove unreferenced components
    * [Revision #3077.188.39](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.39)\
      Fri 2013-05-24 18:17:36 +0200
      * 4371 Maitrayi Sabaratnam 2013-05-23 Bug#13116514 - CREATE LOGFILE GROUP INITIAL\_SIZE & UNDO\_BUFFER\_SIZE FAILS
    * [Revision #3077.188.38](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.38)\
      Fri 2013-05-24 13:58:42 +0300
      * Bug#16859867 INNODB\_BUG14529666 FAILS SPORADICALLY IN VALGRIND
    * [Revision #3077.188.37](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.37) \[merge]\
      Fri 2013-05-24 14:35:00 +0530
      * Bug#16765278 DELETE SQL\_LOAD\_MB\* FILE (TEMP FILE) CREATED BY BINLOG\_KILLED\_SIMULATE.TEST Merging fix from mysql-5.1
      * [Revision #2661.848.41](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.41)\
        Fri 2013-05-24 14:25:00 +0530
        * Bug#16765278 DELETE SQL\_LOAD\_MB\* FILE (TEMP FILE) CREATED BY BINLOG\_KILLED\_SIMULATE.TEST
    * [Revision #3077.188.36](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.36) \[merge]\
      Thu 2013-05-23 15:02:33 +0530
      * Null merge from 5.1 to 5.5
      * [Revision #2661.848.40](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.40)\
        Thu 2013-05-23 15:00:31 +0530
        * Bug #16119355: PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
    * [Revision #3077.188.35](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.35) \[merge]\
      Thu 2013-05-23 11:06:34 +0530
      * Merge from 5.5 to 5.6
      * [Revision #2661.848.39](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.39)\
        Wed 2013-05-22 14:36:43 +0530
        * Bug#11766191:INVALID MEMORY READ IN DO\_DIV\_MOD WITH DOUBLY ASSIGNED VARIABLES Bug#12608543: CRASHES WITH DECIMALS AND STATEMENT NEEDS TO BE REPREPARED ERRORS
    * [Revision #3077.188.34](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.34)\
      Mon 2013-05-20 14:00:40 +0530
    * [Revision #3077.188.33](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.33)\
      Sun 2013-05-19 23:38:06 +0530
      * Bug#16194302: SUPPORT FOR FLOATING-POINT SYSTEM VARIABLES USING THE PLUGIN INTERFACE.
    * [Revision #3077.188.32](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.32)\
      Sat 2013-05-18 10:20:56 +0530
      * Bug #12762377 FOREIGN KEYS NOT CONSTRUCTED WHEN APOSTROPHES ARE ESCAPED WITH BACKSLASH
    * [Revision #3077.188.31](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.31)\
      Fri 2013-05-17 18:54:36 +0530
      * Bug#14236170 MYSQLDUMP 5.5.25 CLIENT FAILS TO DUMP MYSQL DB FROM REMOTE 5.0.96 SERVER
    * [Revision #3077.188.30](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.30)\
      Fri 2013-05-17 08:00:38 +0530
    * [Revision #3077.188.29](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.29)\
      Thu 2013-05-16 18:14:25 +0530
      * BUG #16813006 - UNIT TEST FOR MY\_VSNPRINTF FAIL FOR NON GNU COMPILER
    * [Revision #3077.188.28](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.28)\
      Thu 2013-05-16 11:02:39 +0200
      * Bug#16447483: PARTITION PRUNING IS NOT CORRECT FOR RANGE COLUMNS
    * [Revision #3077.188.27](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.27)\
      Thu 2013-05-16 16:56:02 +0530
      * Fixing a compiler warning issue. At the end of the function ibuf\_insert\_to\_index\_page\_low() add a DBUG\_RETURN(NULL).
    * [Revision #3077.188.26](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.26) \[merge]\
      Thu 2013-05-16 14:34:06 +0530
      * Bug 16813007 5.1 => 5.5 null
      * [Revision #2661.848.38](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.38)\
        Thu 2013-05-16 14:32:09 +0530
        * Bug #16813007 - MTR IS NOT TAKING MYSQLTEST CLIENT USING THE ENV VARIABLE MYSQL\_TEST
    * [Revision #3077.188.25](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.25) \[merge]\
      Thu 2013-05-16 14:19:57 +0530
      * Bug 16813007 5.1 => 5.5
      * [Revision #2661.851.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.851.1)\
        Thu 2013-05-16 14:18:04 +0530
        * Bug #16813007 - MTR IS NOT TAKING MYSQLTEST CLIENT USING THE ENV VARIABLE MYSQL\_TEST
    * [Revision #3077.188.24](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.24) \[merge]\
      Thu 2013-05-16 14:05:51 +0530
      * Null merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.848.37](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.37)\
        Thu 2013-05-16 14:05:05 +0530
        * Bug #16806366 BOGUS CALL TO LOCK\_REC\_RESTORE\_FROM\_PAGE\_INFIMUM IN INSERT BUFFER MERGE
    * [Revision #3077.188.23](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.23) \[merge]\
      Thu 2013-05-16 13:58:26 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.850.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.850.1)\
        Thu 2013-05-16 10:26:09 +0530
        * Bug #16806366 BOGUS CALL TO LOCK\_REC\_RESTORE\_FROM\_PAGE\_INFIMUM IN INSERT BUFFER MERGE
    * [Revision #3077.188.22](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.22) \[merge]\
      Thu 2013-05-16 09:01:11 +0200
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.848.36](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.36)\
        Thu 2013-05-16 08:09:48 +0200
        * Bug#16807394: PREVENT NEW ERROR MESSAGES FROM BEING ADDED TO 5.5
    * [Revision #3077.188.21](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.21)\
      Thu 2013-05-16 13:34:50 +0800
    * [Revision #3077.188.20](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.20)\
      Thu 2013-05-16 10:01:06 +0530
      * Bug #16411457 MASTER THREAD CANNOT EXIT FLUSH\_LOOP WHEN INNODB\_FAST\_SHUTDOWN IS 2
    * [Revision #3077.188.19](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.19) \[merge]\
      Wed 2013-05-15 22:50:44 +0300
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.848.35](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.35)\
        Wed 2013-05-15 22:40:29 +0300
        * Bug#16736929 PAGE\_ZIP\_DECOMPRESS() FAILS ON EMPTY RECORD
    * [Revision #3077.188.18](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.18)\
      Wed 2013-05-15 10:47:19 -0400
      * Bug#16622478 INNODB'S THREAD CONCURRENCY TICKETS MIGHT BE RELEASED AFTER A ROW IS READ
    * [Revision #3077.188.17](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.17)\
      Wed 2013-05-15 07:59:01 +0200
    * [Revision #3077.188.16](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.16)\
      Tue 2013-05-14 22:52:42 +0530
      * Bug#16607258 :Linker Errors Due To Inclusion Of An Implementation File In log\_event.h
    * [Revision #3077.188.15](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.15)\
      Mon 2013-05-13 22:05:56 +0800
      * Bug#14529666 INNODB\_BUFFER\_PAGE DOES NOT MARK CHANGE BUFFER PAGES APPROPRIATELY
    * [Revision #3077.188.14](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.14)\
      Mon 2013-05-13 17:15:25 +0530
      * Bug#12328597 - MULTIPLE COUNT(DISTINCT) IN SAME SELECT FALSE WITH COMPOSITE KEY COLUMNS
    * [Revision #3077.188.13](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.13) \[merge]\
      Mon 2013-05-13 12:27:33 +0530
      * Null merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.848.34](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.34)\
        Mon 2013-05-13 12:01:17 +0530
    * [Revision #3077.188.12](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.12) \[merge]\
      Sun 2013-05-12 19:45:42 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.848.33](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.33)\
        Sun 2013-05-12 19:41:25 +0530
        * Fixing a build issue. In InnoDB plugin, the function innobase\_convert\_to\_filename\_charset() was by mistake kept within the conditional compilation of UNIV\_COMPILE\_TEST\_FUNCS. Now placing the function out of UNIV\_COMPILE\_TEST\_FUNCS. Also, removed the unnecessary log message (as in 5.6+).
    * [Revision #3077.188.11](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.11) \[merge]\
      Fri 2013-05-10 19:21:40 +0530
      * Null merge from 5.1 to 5.5
      * [Revision #2661.848.32](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.32)\
        Fri 2013-05-10 19:18:21 +0530
        * Bug#16119355:PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
    * [Revision #3077.188.10](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.10) \[merge]\
      Fri 2013-05-10 15:38:25 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.848.31](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.31)\
        Fri 2013-05-10 15:35:40 +0530
        * Fixing a build issue. The function innobase\_convert\_to\_system\_charset() is included only in the builtin InnoDB, and it is missed in InnoDB plugin. Adding this function in InnoDB plugin as well.
    * [Revision #3077.188.9](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.9)\
      Thu 2013-05-09 14:01:51 +0530
    * [Revision #3077.188.8](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.8)\
      Wed 2013-05-08 12:52:12 +0200
      * Bug#16779374: NEW ERROR MESSAGE ADDED TO 5.5 AFTER 5.6 GA - REUSING NUMBER ALREADY USED BY 5.6
    * [Revision #3077.188.7](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.7) \[merge]\
      Tue 2013-05-07 18:00:00 +0530
      * Merge from 5.1 to 5.5
      * [Revision #2661.848.30](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.30)\
        Tue 2013-05-07 16:08:48 +0530
        * Bug #16119355: PREPARED STATEMENT: READ OF FREED MEMORY WITH STRING CONVERSION FUNCTIONS
    * [Revision #3077.188.6](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.6) \[merge]\
      Tue 2013-05-07 13:14:01 +0400
      * 5.1 -> 5.5 merge
      * [Revision #2661.848.29](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.29)\
        Tue 2013-05-07 13:10:58 +0400
        * Bug#16095534 CRASH: PREPARED STATEMENT CRASHES IN ITEM\_BOOL\_FUNC2::FIX\_LENGTH\_AND\_DEC The problem happened due to broken left expression in Item\_in\_optimizer object. In case of the bug left expression is runtime created Item\_outer\_ref item which is deleted at the end of the statement and one of Item\_in\_optimizer arguments becomes bad when re-executed. The fix is to use real\_item() instead of original left expression. Note: It feels a bit weird that after preparing, the field is directly part of the generated Item\_func\_eq, whereas in execution it is replaced with an Item\_outer\_ref wrapper object.
    * [Revision #3077.188.5](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.5)\
      Tue 2013-05-07 13:30:25 +0530
      * Bug#16513588:"PREPARE\_COMMIT\_MUTEX" IS NOT FREED DURING TRANSACTION ROLLBACK
    * [Revision #3077.188.4](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.4) \[merge]\
      Mon 2013-05-06 19:57:49 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.848.28](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.28)\
        Mon 2013-05-06 16:28:56 +0530
        * Bug #16722314 FOREIGN KEY ID MODIFIED DURING EXPORT Bug #16754901 PARS\_INFO\_FREE NOT CALLED IN DICT\_CREATE\_ADD\_FOREIGN\_TO\_DICTIONARY
    * [Revision #3077.188.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.3)\
      Mon 2013-05-06 15:01:57 +0200
      * Bug#16757869: INNODB: POSSIBLE REGRESSION IN 5.5.31, BUG#16004999
    * [Revision #3077.188.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.2) \[merge]\
      Mon 2013-05-06 10:56:48 +0200
      * Empty version change upmerge
      * [Revision #2661.848.27](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2661.848.27)\
        Mon 2013-05-06 10:25:03 +0200
        * Raise version number after cloning 5.1.70
    * [Revision #3077.188.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3077.188.1)\
      Mon 2013-05-06 09:51:25 +0200
      * Raise version number after cloning 5.5.32
  * [Revision #3334.1.545](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.545) \[merge]\
    Fri 2013-09-06 10:34:38 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.132](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.132)\
      Fri 2013-09-06 09:55:32 -0700
      * Fixed bug [MDEV-4996](https://jira.mariadb.org/browse/MDEV-4996). The fix for bug [MDEV-4971](https://jira.mariadb.org/browse/MDEV-4971) not always correctly set the pointers to inherited multiple equalities in objects of the Item\_equal class.
  * [Revision #3334.1.544](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.544)\
    Fri 2013-09-06 15:59:19 +0400
    * [MDEV-4978](https://jira.mariadb.org/browse/MDEV-4978) - Server cursor is broken with blobs in the select list, ORDER BY does not work
  * [Revision #3334.1.543](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.543)\
    Tue 2013-09-03 22:45:12 +0200
    * [MDEV-4926](https://jira.mariadb.org/browse/MDEV-4926): Remove division-using-subtraction implementation from semi-sync plugin
  * [Revision #3334.1.542](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.542) \[merge]\
    Tue 2013-09-03 18:41:07 +0400
    * [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Merge into 5.5-main
    * [Revision #3334.46.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.46.2)\
      Wed 2013-08-28 21:21:12 +0400
      * [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942): Add another testcase after merging with other fixes.
    * [Revision #3334.46.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.46.1) \[merge]\
      Wed 2013-08-28 20:31:23 +0400
      * Automatic merge of [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836) fix into 5.5
      * [Revision #3334.45.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.45.2)\
        Mon 2013-08-26 21:38:04 +0400
        * Fix for [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836) fix: take into account situation where "notnull\_col IS NULL" is not a direct child of the WHERE clause item, but rather is embedded inside Item\_cond\_and or Item\_cond\_or.
      * [Revision #3334.45.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.45.1) \[merge]\
        Mon 2013-08-26 16:31:58 +0400
        * Fix for [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Merge with current 5.5
        * [Revision #3334.44.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.44.1)\
          Fri 2013-08-23 16:32:56 +0400
          * [MDEV-4836](https://jira.mariadb.org/browse/MDEV-4836): Wrong result on IS NULL (old documented hack stopped working) - When applying optimization introduced by [MDEV-4817](https://jira.mariadb.org/browse/MDEV-4817), ignore the conditions that have form "datetime\_not\_null\_col IS NULL".
  * [Revision #3334.1.541](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.541) \[merge]\
    Sat 2013-08-31 09:33:09 -0700
    * Merge
    * [Revision #3334.43.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.43.1) \[merge]\
      Sat 2013-08-31 08:18:25 -0700
      * Merge 5.3->5.5
      * [Revision #2502.567.131](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.131)\
        Thu 2013-08-29 21:02:42 -0700
        * Fixed bug [MDEV-4971](https://jira.mariadb.org/browse/MDEV-4971). The function propagate\_new\_equalities() did not updated properly the references to inherited multiple equalities.
  * [Revision #3334.1.540](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.540)\
    Fri 2013-08-30 11:00:29 +0400
    * [MDEV-4902](https://jira.mariadb.org/browse/MDEV-4902) - sql\_yacc.yy incompatible with bison 3
  * [Revision #3334.1.539](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.539) \[merge]\
    Thu 2013-08-29 12:32:09 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.130](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.130)\
      Thu 2013-08-29 10:56:12 -0700
      * Fixed bug [MDEV-4962](https://jira.mariadb.org/browse/MDEV-4962). When a non-nullable datetime field is used under an IS NULL predicate of the WHERE condition in a query with outer joins the remove\_eq\_conds function should check whether this field belongs to an inner table of any outer join that can be, in a general case, a nested outer join.
  * [Revision #3334.1.538](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.538)\
    Wed 2013-08-28 22:16:13 +0200
    * fix an old bug where dd\_frm\_type() could incorrectly determine the table type for dynamic engines (because it only looked at the one-byte code, not at the full engine name).
  * [Revision #3334.1.537](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.537)\
    Wed 2013-08-28 22:16:03 +0200
    * Test case for MyISAM and OPTIMIZE TABLE that requires MDL\_SHARED\_NO\_READ\_WRITE.
  * [Revision #3334.1.536](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.536)\
    Mon 2013-08-26 21:14:34 +0400
    * bugfix: storage engine might return a negative error code, but it shouldn't be ignored on return
  * [Revision #3334.1.535](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.535)\
    Mon 2013-08-26 21:14:01 +0400
    * mtr bug: files outside of both the suite dir and the overlay dir, were treated as coming from the overlay.
  * [Revision #3334.1.534](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.534)\
    Mon 2013-08-26 21:13:17 +0400
    * don't decide on extended keys by DB\_TYPE\_INNODB, use hton->flags
  * [Revision #3334.1.533](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.533)\
    Mon 2013-08-26 21:04:10 +0400
    * HA\_ERR\_TABLE\_DEF\_CHANGED is normal situation, not an server-wide exception, don't log it to the error log.
  * [Revision #3334.1.532](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.532)\
    Mon 2013-08-26 21:03:01 +0400
    * typo fixed (boolean index attributes didn't work)
  * [Revision #3334.1.531](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.531)\
    Wed 2013-08-28 07:49:53 +0200
    * [MDEV-4951](https://jira.mariadb.org/browse/MDEV-4951) drop user leaves privileges
  * [Revision #3334.1.530](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.530)\
    Wed 2013-08-28 09:14:57 -0700
    * Fixed bug [MDEV-4959](https://jira.mariadb.org/browse/MDEV-4959). The fix for [MDEV-4420](https://jira.mariadb.org/browse/MDEV-4420) was not quite correct. This patch corrects it.
  * [Revision #3334.1.529](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.529) \[merge]\
    Tue 2013-08-27 22:19:14 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.129](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.129)\
      Mon 2013-08-26 15:51:47 -0700
      * Fixed bug [MDEV-4952](https://jira.mariadb.org/browse/MDEV-4952) When in function remove\_eq\_conds() a sub-formula of the processed condition is replaced for another formula we should ensure that in the resulting formula AND/OR levels must alternate.
    * [Revision #2502.567.128](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.128)\
      Mon 2013-08-26 12:55:58 -0700
      * Fixed bug [MDEV-4944](https://jira.mariadb.org/browse/MDEV-4944). The patch to fix [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) turned out to be incorrect. At the substitution of single row tables in make\_join\_statistics() the used multiple equalities may change and references to the new multiple equalities must be updated. The function remove\_eq\_conds() takes care of it and it should be called right after the substitution of single row tables. Calling it after the call of make\_join\_statistics was a mistake.
  * [Revision #3334.1.528](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.528)\
    Tue 2013-08-27 19:18:04 +0300
    * Fixed MySQL bug #69861 LAST\_INSERT\_ID is replicated incorrectly if replication filters are used
  * [Revision #3334.1.527](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.527) \[merge]\
    Mon 2013-08-26 16:23:14 +0400
    * Merge fix for [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942), 5.3->5.5
    * [Revision #2502.567.127](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.127)\
      Fri 2013-08-23 22:17:02 -0700
      * Fixed bug [MDEV-4942](https://jira.mariadb.org/browse/MDEV-4942). Made sure that degenerate conjunctions/disjunctions are obtained from AND/OR conditions.
  * [Revision #3334.1.526](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.526) \[merge]\
    Fri 2013-08-23 08:34:35 -0700
    * Merge
    * [Revision #3334.42.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.42.1)\
      Fri 2013-08-23 07:25:45 -0700
      * Fixed bug [MDEV-4420](https://jira.mariadb.org/browse/MDEV-4420). The code of JOIN::optimize that performed substitutions for the best equal field in all ref items did not take into account that a multiple equality could contain the result of the single-value subquery if the subquery is inexpensive. This code was corrected. Also made necessary corresponding corrections in the code of make\_join\_select().
  * [Revision #3334.1.525](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.525) \[merge]\
    Thu 2013-08-22 16:23:54 +0400
    * Merging from 5.3
    * [Revision #2502.567.126](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.126)\
      Thu 2013-08-22 15:20:27 +0400
      * [MDEV-4804](https://jira.mariadb.org/browse/MDEV-4804) Date comparing false result
  * [Revision #3334.1.524](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.524) \[merge]\
    Thu 2013-08-22 14:13:46 +0400
    * Automatic merge
    * [Revision #3334.41.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.41.1)\
      Thu 2013-08-22 14:12:10 +0400
      * [MDEV-4840](https://jira.mariadb.org/browse/MDEV-4840): Wrong result (missing rows) on LEFT JOIN with InnoDB tables Fix two problems in table elimination code: - Before marking a "value" as bound, check if it is already bound. Marking the same value as bound twice could confuse a module that depends on this value, because Dep\_module\_XXX use counters to know when they become bound.
  * [Revision #3334.1.523](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.523) \[merge]\
    Wed 2013-08-21 12:34:58 -0700
    * Merge
    * [Revision #2502.567.125](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.125)\
      Wed 2013-08-21 17:42:09 +0300
      * [MDEV-4908](https://jira.mariadb.org/browse/MDEV-4908): Assertion \`((Item\_cond \*) cond)->functype() == ((Item\_cond \*) new\_item)->functype()' fails on a query with IN and equal conditions, AND/OR, materialization+semijoin
  * [Revision #3334.1.522](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.522) \[merge]\
    Wed 2013-08-21 11:27:02 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.124](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.124)\
      Tue 2013-08-20 13:47:13 -0700
      * Fixed a bug/typo in the patch for [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355), noticed after the patch had been merged into 5.5.
    * [Revision #2502.567.123](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.123)\
      Tue 2013-08-20 17:08:03 +0300
      * Fix bug [MDEV-4895](https://jira.mariadb.org/browse/MDEV-4895) Valgrind warnings (Conditional jump or move depends on uninitialised value) in Field\_datetime::get\_date on GREATEST(..) IS NULL
    * [Revision #2502.567.122](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.122)\
      Mon 2013-08-19 14:24:48 -0700
      * Backported from maria-5.5 the fix in the patch for [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) that had been discovered when merging the patch from 5.3 into 5.5.
  * [Revision #3334.1.521](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.521)\
    Tue 2013-08-20 16:05:34 +0300
    * [MDEV-4923](https://jira.mariadb.org/browse/MDEV-4923) Incorrect merge on XtraDB os0file.c. Function os\_file\_set\_atomic\_writes returns TRUE when successfull and FALSE at failure.
  * [Revision #3334.1.520](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.520)\
    Tue 2013-08-20 10:42:38 +0200
    * Backport from 10.0-base fix for tests failing when vardir has no execute permissions.
  * [Revision #3334.1.519](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.519) \[merge]\
    Mon 2013-08-19 08:55:49 -0700
    * Merge
    * [Revision #3334.40.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.40.2) \[merge]\
      Sun 2013-08-18 22:13:49 -0700
      * Merge
    * [Revision #3334.40.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.40.1) \[merge]\
      Sun 2013-08-18 19:58:51 -0700
      * Merge 5.3->5.5. In particular: Merged the patch for bug [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418) from 5.3 into 5.5. Fixed a bug in the patch that should be backported to 5.3.
      * [Revision #2502.567.121](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.121)\
        Fri 2013-08-16 22:01:47 -0700
        * Fixed bug [MDEV-4418](https://jira.mariadb.org/browse/MDEV-4418). After single row substitutions there might appear new equalities. They should be properly propagated to all AND/OR levels the WHERE condition. It's done now with an additional call of remove\_eq\_conds().
      * [Revision #2502.567.120](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.120) \[merge]\
        Thu 2013-08-15 16:59:20 -0700
        * Merge
        * [Revision #2502.578.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.578.1)\
          Thu 2013-08-15 14:16:16 -0700
          * Fixed bug [MDEV-4355](https://jira.mariadb.org/browse/MDEV-4355). This patch almost totally revised the patch for bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177). The latter had too many defects. In particular, it did not propagate multiple equalities formed when merging a degenerate disjunct into underlying AND formula.
      * [Revision #2502.567.119](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.119) \[merge]\
        Thu 2013-08-15 14:04:20 -0700
        * Merge 5.2->5.3
        * [Revision #2502.566.53](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.53) \[merge]\
          Wed 2013-08-14 20:37:38 -0700
          * Merge 5.1->5.2
          * [Revision #2502.565.53](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.53)\
            Tue 2013-08-13 15:21:11 -0700
            * Fixed bug [MDEV-4894](https://jira.mariadb.org/browse/MDEV-4894). This a an old legacy performance bug. When a very selective range scan existed for the second table in a join, and, at the same time, there was another range condition depending on the fields of the first table, the optimizer chose a plan with 'Range checked for each record'. This plan was extremely inefficient in comparison with the regular selective range scan. As a matter of fact the range scan chosen for each record was the same as that selective range scan.
          * [Revision #2502.565.52](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.565.52)\
            Mon 2013-07-22 00:55:06 +0500
            * [MDEV-4478](https://jira.mariadb.org/browse/MDEV-4478) check mysql-5.5 changes in spatial.cc. not\_enough\_points() introduced to check if the spatial object is incorrect.
        * [Revision #2502.566.52](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.566.52)\
          Thu 2013-08-01 09:25:50 +0300
          * [MDEV-4823](https://jira.mariadb.org/browse/MDEV-4823): Server crashes in Item\_func\_not::fix\_fields on creating a table with a virtual column using NOT
  * [Revision #3334.1.518](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.518)\
    Sat 2013-08-17 17:20:09 +0400
    * [MDEV-4165](https://jira.mariadb.org/browse/MDEV-4165) \[PATCH] RFE: make tmpdir a build-time configurable option
  * [Revision #3334.1.517](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.517)\
    Wed 2013-08-14 11:12:57 +0200
    * fix a comment
  * [Revision #3334.1.516](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.516) \[merge]\
    Mon 2013-08-12 17:33:08 +0400
    * Merge from 5.3
    * [Revision #2502.567.118](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.118)\
      Mon 2013-08-12 16:47:59 +0400
      * [MDEV-4652](https://jira.mariadb.org/browse/MDEV-4652) Wrong result for CONCAT(GREATEST(TIME('00:00:01'),TIME('00:00:00'))
    * [Revision #2502.567.117](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.117)\
      Thu 2013-08-01 11:46:11 +0300
      * [MDEV-4811](https://jira.mariadb.org/browse/MDEV-4811) Assertion \`offset < 0x1f' fails in type\_and\_offset\_store on COLUMN\_ADD [MDEV-4812](https://jira.mariadb.org/browse/MDEV-4812) Valgrind warnings (Invalid write) in dynamic\_column\_update\_many on COLUMN\_ADD
  * [Revision #3334.1.515](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.515)\
    Thu 2013-08-08 13:33:15 +0200
    * `mysql --skip-column-names` flag should not affect alignment of field values, set num\_flag\[] unconditionally, not under "if (column\_names)"
  * [Revision #3334.1.514](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.514) \[merge]\
    Thu 2013-08-08 13:41:21 +0400
    * Merge from 5.3
    * [Revision #2502.567.116](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.116)\
      Thu 2013-08-08 12:58:28 +0400
      * [MDEV-4653](https://jira.mariadb.org/browse/MDEV-4653) Wrong result for CONVERT\_TZ(TIME('00:00:00'),'+00:00','+7:5')
  * [Revision #3334.1.513](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.513) \[merge]\
    Thu 2013-08-08 11:48:49 +0400
    * Merge from 5.3
    * [Revision #2502.567.115](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/2502.567.115)\
      Thu 2013-08-08 11:36:03 +0400
      * [MDEV-4512](https://jira.mariadb.org/browse/MDEV-4512) Valgrind warnings in my\_long10\_to\_str\_8bit on INTERVAL and DATE\_ADD with incorrect types Fixing a typo: bit AND (&) was erroneously used instead of logical AND (&&)
  * [Revision #3334.1.512](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.512)\
    Mon 2013-08-05 17:34:38 +0300
    * Fix possible race condition in Query cache.
  * [Revision #3334.1.511](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.511) \[merge]\
    Mon 2013-08-05 20:59:15 +0400
    * Automatic merge
    * [Revision #3334.39.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.39.1)\
      Mon 2013-08-05 20:57:48 +0400
      * Update test results after fix for [MDEV-4687](https://jira.mariadb.org/browse/MDEV-4687)
  * [Revision #3334.1.510](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.510) \[merge]\
    Mon 2013-08-05 21:21:21 +0400
    * Fixes for storage\_engine tests diverged from the main line
    * [Revision #3334.38.3](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.38.3)\
      Mon 2013-08-05 20:31:29 +0400
      * Deliberate change in behavior introduced in MySQL 5.5.31 along with the partitioning enhancement for Bug#14521864
    * [Revision #3334.38.2](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.38.2)\
      Mon 2013-08-05 18:42:22 +0400
      * The test was non-deterministic while choosing an alternative storage engine
    * [Revision #3334.38.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.38.1)\
      Mon 2013-08-05 18:30:12 +0400
      * Deliberate change in behavior introduced along with the fix for [MDEV-4310](https://jira.mariadb.org/browse/MDEV-4310)
  * [Revision #3334.1.509](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.509)\
    Wed 2013-07-31 17:24:52 +0400
    * [MDEV-4817](https://jira.mariadb.org/browse/MDEV-4817): Optimizer fails to optimize expression of the form 'FOO' IS NULL - Modify the way Item\_cond::fix\_fields() and Item\_cond::eval\_not\_null\_tables() calculate bitmap for Item\_cond\_or::not\_null\_tables(): if they see a "... OR inexpensive\_const\_false\_item OR ..." then the item can be ignored. - Updated test results. There can be more warnings produced since parts of WHERE are evaluated more times.
  * [Revision #3334.1.508](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.508) \[merge]\
    Wed 2013-07-31 13:37:01 +0400
    * Automatic merge
    * [Revision #3334.37.1](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.37.1)\
      Thu 2013-07-25 22:42:26 +0400
      * [MDEV-4687](https://jira.mariadb.org/browse/MDEV-4687): impossible where with < operation, but =-5 return one row - Let \_ma\_record\_pos() set SEARCH\_PART\_KEY when doing a search on a prefix of a \[unique] key. Otherwise, \_ma\_search\_pos() would find the first key equal to search key, and assume it is also the last one, which will make a wrong estimate of key's position.
  * [Revision #3334.1.507](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.507)\
    Mon 2013-07-29 16:03:41 +0200
    * [MDEV-4815](https://jira.mariadb.org/browse/MDEV-4815) - allow multiple mysql\_server\_init() / mysql\_server\_end() in the same process, for embedded library.
  * [Revision #3334.1.506](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.506)\
    Fri 2013-07-19 13:21:23 +0300
    * Revert reverted patch (as workaround) to have no problem with ongoing fix.
  * [Revision #3334.1.505](https://bazaar.launchpad.net/~maria-captains/maria/maria-5.5-galera/revision/3334.1.505)\
    Thu 2013-07-18 11:16:18 +0300
    * Fix of using uninitialized variadle.

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
