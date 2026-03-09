# MariaDB 5.5.28a Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.28a) | [Release Notes](../../old-releases/5.5/5.5.28a.md) | **Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 29 Nov 2012

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.28a.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3587](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3587)\
  Tue 2012-11-27 12:26:15 +0100
  * 5.5.28a
* [Revision #3586](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3586)\
  Tue 2012-11-27 15:47:08 +0100
  * Fix yet another regression after [MDEV-3885](https://jira.mariadb.org/browse/MDEV-3885). If connection kills itself (or own query), it will get an error consistently, with both COM\_PROCESSKILL and with "KILL \[QUERY] id"
* [Revision #3585](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3585)\
  Tue 2012-11-27 12:34:13 +0100
  * fix regression in sp\_notembedded after [MDEV-3885](https://jira.mariadb.org/browse/MDEV-3885)
* [Revision #3584](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3584)\
  Tue 2012-11-27 00:45:29 +0100
  * [MDEV-3885](https://jira.mariadb.org/browse/MDEV-3885) - connection suicide via mysql\_kill() causes assertion in server
* [Revision #3583](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3583)\
  Mon 2012-11-26 18:50:29 +0100
  * mysql-test: sys\_vars stub for a new xtradb config variable; tc\_log\_mmap test;
* [Revision #3582](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3582) \[merge]\
  Thu 2012-11-22 11:43:55 +0100
  * XtraDB from Percona-Server-5.5.28-rel29.1
  * [Revision #0.12.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.58)\
    Wed 2012-11-21 23:25:38 +0100
    * bzr ignore 'Percona-Server-\*.tar.gz'
  * [Revision #0.12.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.57)\
    Wed 2012-11-21 23:24:18 +0100
    * Percona-Server-5.5.28-rel29.1.tar.gz
* [Revision #3581](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3581) \[merge]\
  Thu 2012-11-22 10:19:31 +0100
  * 5.3->5.5 merge
  * [Revision #2502.567.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.47)\
    Sat 2012-11-17 16:50:15 +0100
    * [MDEV-736](https://jira.mariadb.org/browse/MDEV-736) [Bug #1004615](https://bugs.launchpad.net/bugs/1004615) - Unexpected warnings "Encountered illegal value '' when converting to DECIMAL" on a query with aggregate functions and GROUP BY
  * [Revision #2502.567.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.46) \[merge]\
    Tue 2012-11-20 13:57:49 +0100
    * Merge [MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)->5.3
    * [Revision #2502.566.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.25) \[merge]\
      Tue 2012-11-20 13:40:13 +0100
      * Merge [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)->5.2.
      * [Revision #2502.565.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.20)\
        Tue 2012-11-20 13:28:53 +0100
        * [MDEV-3861](https://jira.mariadb.org/browse/MDEV-3861): assertions in TC\_LOG\_MMAP.
      * [Revision #2502.565.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.19)\
        Mon 2012-11-19 11:18:40 +0100
        * potential crash in the feedback plugin
      * [Revision #2502.565.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.18)\
        Sat 2012-11-17 19:04:13 +0100
        * [MDEV-3850](https://jira.mariadb.org/browse/MDEV-3850) too early pthread\_mutex\_unlock in TC\_LOG\_MMAP::log\_xid
      * [Revision #2502.565.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.17)\
        Mon 2012-11-12 19:56:51 +0100
        * followup fixes for MySQL Bug #13889741: HANDLE\_FATAL\_SIGNAL IN _DB\_ENTER_ | HANDLE\_FATAL\_SIGNAL IN STRNLEN
      * [Revision #2502.565.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.16)\
        Sat 2012-11-10 20:36:18 +0100
        * [MDEV-3849](https://jira.mariadb.org/browse/MDEV-3849) - 1 bytes stack overwrite in normalize\_dirname().
      * [Revision #2502.565.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.15)\
        Fri 2012-11-09 20:15:23 +0100
        * add a test case for MySQL Bug #13889741: HANDLE\_FATAL\_SIGNAL IN _DB\_ENTER_ | HANDLE\_FATAL\_SIGNAL IN STRNLEN
    * [Revision #2502.566.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.24)\
      Fri 2012-11-09 23:51:51 -0800
      * Fixed bug [MDEV-3845](https://jira.mariadb.org/browse/MDEV-3845). If triggers are used for an insert/update/delete statement than the values of all virtual columns must be computed as any of them may be used by the triggers.
  * [Revision #2502.567.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.45)\
    Mon 2012-11-19 18:17:46 +0200
    * [MDEV-3801](https://jira.mariadb.org/browse/MDEV-3801) Adjust unstable test case.
  * [Revision #2502.567.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.44)\
    Mon 2012-11-19 15:38:27 +0200
    * [MDEV-3801](https://jira.mariadb.org/browse/MDEV-3801) Reproducible sub select join crash on 5.3.8 and 5.3.9
  * [Revision #2502.567.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.43)\
    Sat 2012-11-10 00:10:06 +0200
    * Increase the version number to 5.3.10.
  * [Revision #2502.567.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.42)\
    Sat 2012-11-10 00:04:44 +0200
    * adjusted test result
  * [Revision #2502.567.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.41)\
    Fri 2012-11-09 15:27:13 +0200
    * adjust openssl\_1 test as in 5.2 (no idea why this didn't merge)
  * [Revision #2502.567.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.40)\
    Fri 2012-11-09 13:07:32 +0200
    * [MDEV-3810](https://jira.mariadb.org/browse/MDEV-3810) fix.
  * [Revision #2502.567.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.39) \[merge]\
    Fri 2012-11-09 13:05:05 +0200
    * merge from 5.2
    * [Revision #2502.566.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.23)\
      Fri 2012-11-09 12:49:12 +0200
      * Disable PBXT on Windows to match all other platforms.
  * [Revision #2502.567.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.38) \[merge]\
    Fri 2012-11-09 12:54:48 +0200
    * merge test case adjustments from 5.2
    * [Revision #2502.566.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.22)\
      Fri 2012-11-09 11:56:27 +0200
      * Removed the dependency on PBXT from tests information\_schema\_all\_engines, and is\_columns\_is. Made information\_schema\_all\_engines stable by adding "sorted\_result".
  * [Revision #2502.567.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.37) \[merge]\
    Fri 2012-11-09 10:47:33 +0200
    * Merge from 5.2
    * [Revision #2502.566.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.21)\
      Thu 2012-11-08 23:18:56 +0100
      * Fix mis-merge.
  * [Revision #2502.567.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.36) \[merge]\
    Fri 2012-11-09 10:11:20 +0200
    * Merge [MariaDB 5.1.66](../../old-releases/5.1/5.1.66.md) -> 5.2 -> 5.3
    * [Revision #2502.566.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.20) \[merge]\
      Thu 2012-11-08 22:26:05 +0200
      * Merged and adjusted test cases from 5.1 after the merge with 5.1.
      * [Revision #2502.565.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.14)\
        Wed 2012-11-07 17:48:02 +0200
        * Updated test results after the mysql 5.1 merge.
    * [Revision #2502.566.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.19) \[merge]\
      Thu 2012-11-08 15:24:35 +0200
      * Merge [MariaDB 5.1.66](../../old-releases/5.1/5.1.66.md) -> 5.2.12
      * [Revision #2502.565.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.13) \[merge]\
        Tue 2012-11-06 11:52:55 +0200
        * Merge MySQL 5.1.66 -> MariaDB 5.1.65
        * [Revision #2661.817.84](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.84)\
          Tue 2012-09-11 12:47:32 +0200
          * Spec file change to work around cast ulonglong -> int.
        * [Revision #2661.817.83](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.83)\
          Wed 2012-09-05 17:40:13 +0200
          * Bug#13734987 MEMORY LEAK WITH I\_S/SHOW AND VIEWS WITH SUBQUERY
        * [Revision #2661.817.82](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.82)\
          Mon 2012-09-03 11:33:05 +0530
        * [Revision #2661.817.81](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.81)\
          Fri 2012-08-31 15:42:00 +0530
          * Bug #13453036 ERROR CODE 1118: ROW SIZE TOO LARGE - EVEN THOUGH IT IS NOT.
        * [Revision #2661.817.80](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.80)\
          Fri 2012-08-31 09:51:27 +0300
        * [Revision #2661.817.79](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.79)\
          Thu 2012-08-30 21:53:41 +0300
          * Bug#14554000 CRASH IN PAGE\_REC\_GET\_NTH\_CONST(NTH=0) DURING COMPRESSED PAGE SPLIT
        * [Revision #2661.817.78](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.78)\
          Thu 2012-08-30 21:49:24 +0300
          * Bug#14547952: DEBUG BUILD FAILS ASSERTION IN RECORDS\_IN\_RANGE()
        * [Revision #2661.817.77](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.817.77)\
          Tue 2012-08-28 14:51:01 +0200
          * Bug#14547952: DEBUG BUILD FAILS ASSERTION IN RECORDS\_IN\_RANGE()
      * [Revision #2502.565.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.12) \[merge]\
        Thu 2012-11-01 16:20:09 +0100
        * Merge XtraDB from Percona-Server 5.1.66-rel14.1 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md).
        * [Revision #0.16.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.16.2)\
          Thu 2012-11-01 15:16:42 +0100
          * Updated with changes from Percona Server 5.1.66-rel14.1 tarball.
    * [Revision #2502.566.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.18)\
      Fri 2012-11-02 08:21:03 +0100
      * Update result file now we no longer build PBXT.
  * [Revision #2502.567.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.35) \[merge]\
    Fri 2012-11-02 15:59:16 -0700
    * Merge.
    * [Revision #2502.569.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.569.1)\
      Thu 2012-11-01 14:54:33 -0700
      * Fixed bug [MDEV-585](https://jira.mariadb.org/browse/MDEV-585) (LP bug #637962) If, when executing a query with ORDER BY col LIMIT n, the optimizer chose an index-merge scan to access the table containing col while there existed an index defined over col then optimizer did not consider the possibility of using an alternative range scan by this index to avoid filesort. This could cause a performance degradation if the optimizer flag index\_merge was set up to 'on'.
  * [Revision #2502.567.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.34) \[merge]\
    Fri 2012-11-02 15:35:09 +0400
    * Merge: bzr ignore sql-bench/test-table-elimination
    * [Revision #2502.568.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.568.1)\
      Fri 2012-11-02 15:31:54 +0400
      * bzr ignore sql-bench/test-table-elimination
  * [Revision #2502.567.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.33) \[merge]\
    Thu 2012-11-01 21:36:31 +0200
    * Merge 5.2 -> 5.3
    * [Revision #2502.566.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.17) \[merge]\
      Thu 2012-11-01 15:44:34 +0200
      * Merge 5.1 -> 5.2
      * [Revision #2502.565.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.11)\
        Wed 2012-10-31 23:49:51 +0200
        * Fixed [MDEV-612](https://jira.mariadb.org/browse/MDEV-612), [Bug #1010759](https://bugs.launchpad.net/bugs/1010759) - Valgrind error ha\_maria::check\_if\_incompatible\_data on
      * [Revision #2502.565.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.10)\
        Wed 2012-10-31 23:22:32 +0200
        * Fixed [MDEV-647](https://jira.mariadb.org/browse/MDEV-647),[Bug #986261](https://bugs.launchpad.net/bugs/986261) - Aria unit tests fail at ma\_test2
    * [Revision #2502.566.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.16)\
      Thu 2012-11-01 00:06:09 +0200
      * Fix of non-deterministic results.
    * [Revision #2502.566.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.15)\
      Wed 2012-10-31 23:04:53 +0200
      * Do not build pbxt.
    * [Revision #2502.566.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.14)\
      Tue 2012-10-09 17:36:02 +0300
      * [MDEV-616](https://jira.mariadb.org/browse/MDEV-616) fix (MySQL fix accepted)
    * [Revision #2502.566.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.13)\
      Sun 2012-10-14 19:29:31 +0300
      * [MDEV-746](https://jira.mariadb.org/browse/MDEV-746): Merged mysql fix of the bug [Bug #1002546](https://bugs.launchpad.net/bugs/1002546) & MySQL Bug#13651009.
    * [Revision #2502.566.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.12)\
      Tue 2012-10-02 12:53:20 +0300
      * fixed [MDEV-568](https://jira.mariadb.org/browse/MDEV-568): Wrong result for a hash index look-up if the index is unique and the key is NULL
  * [Revision #2502.567.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.32)\
    Wed 2012-10-31 09:34:25 +0400
    * [MDEV-772](https://jira.mariadb.org/browse/MDEV-772), [MDEV-744](https://jira.mariadb.org/browse/MDEV-744): Fix test-table-elimination script to work.
* [Revision #3580](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3580)\
  Thu 2012-11-15 19:20:10 +0100
  * [MDEV-3826](https://jira.mariadb.org/browse/MDEV-3826) compilation of client programs fail: m\_string.h tries to include \<mysql/plugin.h>
* [Revision #3579](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3579)\
  Thu 2012-11-08 16:49:07 +0100
  * [MDEV-259](https://jira.mariadb.org/browse/MDEV-259) audit plugin does not see sub-statements
* [Revision #3578](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3578)\
  Thu 2012-11-08 14:17:53 +0100
  * [MDEV-258](https://jira.mariadb.org/browse/MDEV-258) audit plugin only see queries if general log is enabled
* [Revision #3577](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3577)\
  Wed 2012-11-07 19:07:47 +0100
  * rename plugin null\_audit -> audit\_null (to match status variable names) create audit\_null.test
* [Revision #3576](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3576)\
  Tue 2012-11-20 15:24:39 +0100
  * [MDEV-3868](https://jira.mariadb.org/browse/MDEV-3868) : windows client compilation issues
* [Revision #3575](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3575)\
  Mon 2012-11-19 19:29:27 -0800
  * Fixed bug [MDEV-622](https://jira.mariadb.org/browse/MDEV-622) (LP bug #1002508). Back-ported the fix and the test case for bug 13528826 from mysql-5.6.
* [Revision #3574](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3574)\
  Sun 2012-11-11 11:47:44 -0800
  * Fixed bug [MDEV-3851](https://jira.mariadb.org/browse/MDEV-3851). Any ref access to a table by a key fully extended by the components of the primary key should be actually an eq\_ref access.
* [Revision #3573](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3573)\
  Tue 2012-11-06 18:09:26 +0100
  * build feedback plugin with ssl (changes for cmake). fix the ssl related code to use newer function prototypes
* [Revision #3572](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3572)\
  Tue 2012-11-06 23:18:07 -0800
  * Added the test case for bug #54599 into mariadb code line. The fix for this bug was pulled from mysql-5.5 earlier.
* [Revision #3571](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3571)\
  Sun 2012-11-04 22:20:04 +0100
  * [MDEV-3830](https://jira.mariadb.org/browse/MDEV-3830) - fix compilation for Intel compiler, avoid .cfi\_escape , 32 bit code.
* [Revision #3570](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3570)\
  Sun 2012-11-04 19:09:46 +0400
  * [MDEV-536](https://jira.mariadb.org/browse/MDEV-536): [Bug #1050806](https://bugs.launchpad.net/bugs/1050806) - different result for a query using subquery, and [MDEV-567](https://jira.mariadb.org/browse/MDEV-567): Wrong result from a query with correlated subquery if ICP is allowed:
* [Revision #3569](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3569)\
  Sat 2012-11-03 00:31:50 +0100
  * [MDEV-3830](https://jira.mariadb.org/browse/MDEV-3830) - fix build on Intel compiler
* [Revision #3568](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3568)\
  Fri 2012-11-02 10:43:52 +0100
  * [MDEV-531](https://jira.mariadb.org/browse/MDEV-531) : Warning: Forcing close of thread ... in rpl\_binlog\_index
* [Revision #3567](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3567)\
  Wed 2012-10-31 12:47:25 +0100
  * Fix crashes on 32-bit async client lib when -fomit-frame-pointer
* [Revision #3566](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3566)\
  Tue 2012-10-30 23:05:55 +0100
  * [MDEV-672](https://jira.mariadb.org/browse/MDEV-672) : storage/maria and storage/perfschema do not appear to honor WITH\_UNIT\_TESTS
* [Revision #3565](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3565)\
  Tue 2012-10-30 19:13:39 +0100
  * [MDEV-3824](https://jira.mariadb.org/browse/MDEV-3824) - xtradb file rename fails on Windows, if new name already exists.
* [Revision #3564](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3564)\
  Sat 2012-10-27 00:56:14 +0300
  * [MDEV-3812](https://jira.mariadb.org/browse/MDEV-3812)
* [Revision #3563](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3563)\
  Thu 2012-10-25 15:50:10 +0300
  * [MDEV-3812](https://jira.mariadb.org/browse/MDEV-3812): Remove unneeded extra call to engine->exec() in Item\_subselect::exec, remove enum store\_key\_result

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
